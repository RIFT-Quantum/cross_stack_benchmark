"""Offline regression checks for the notebook; never authenticate or submit jobs."""
import ast
import json
import unittest
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from qiskit import QuantumCircuit
from qiskit.primitives.containers import SamplerPub


NOTEBOOK = Path(__file__).resolve().parents[1] / "retrieve_ibm_job_metadata.ipynb"


class Backend:
    name = "ibm_test"

    def __init__(self, snapshot=None):
        self.snapshot = snapshot
        self.lookup_dates = []

    def properties(self, *, datetime):
        self.lookup_dates.append(datetime)
        return self.snapshot


class Job:
    creation_date = datetime(2026, 7, 1, tzinfo=timezone.utc)
    primitive_id = "sampler"
    session_id = None
    image = "historical-runtime"
    tags = []
    usage_estimation = {}
    inputs = {"pubs": []}

    def __init__(self, backend):
        self.device = backend

    def backend(self, timeout=None):
        return self.device

    def status(self):
        return "DONE"

    def metrics(self):
        return {"timestamps": {"running": "2026-07-02T00:00:00Z"}}


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.nb = json.loads(NOTEBOOK.read_text())
        self.ns = {"INCLUDE_BACKEND_PROPERTIES": True}
        exec("".join(self.nb["cells"][6]["source"]), self.ns)
        self.snapshot = {
            "backend_name": "ibm_test",
            "last_update_date": datetime(2026, 7, 1, tzinfo=timezone.utc),
            "qubits": [],
        }
        self.backend = Backend(self.snapshot)

    def test_partial_metadata_survives_missing_inputs_and_metrics(self):
        class PartialJob(Job):
            @property
            def inputs(self):
                raise RuntimeError("Inputs expired")

            def metrics(self):
                raise RuntimeError("Metrics unavailable")

        result = self.ns["retrieve_runtime_job"](PartialJob(self.backend), "j")
        self.assertEqual(result["backend_name"], "ibm_test")
        self.assertEqual(result["status"], "DONE")
        self.assertEqual(result["retrieval_status"], "partial")
        self.assertEqual(set(result["field_errors"]), {"inputs", "metrics"})
        self.assertEqual(result["backend_calibration"]["status"], "retrieved")
        self.assertEqual(result["backend_calibration"]["lookup_time_source"], "submission_time_fallback")

    def test_execution_timestamp_and_snapshot_deduplication(self):
        first = self.ns["retrieve_runtime_job"](Job(self.backend), "a")["backend_calibration"]
        second = self.ns["retrieve_runtime_job"](Job(self.backend), "b")["backend_calibration"]
        self.assertEqual(first["lookup_time_source"], "execution_start")
        self.assertEqual(first["lookup_time_utc"], "2026-07-02T00:00:00+00:00")
        self.assertEqual(self.backend.lookup_dates[0], datetime(2026, 7, 2, tzinfo=timezone.utc))
        self.assertEqual(first["snapshot_id"], second["snapshot_id"])
        self.assertEqual(len(self.ns["calibration_snapshots"]), 1)

    def test_calibration_states_and_no_undated_current_lookup(self):
        retrieve = self.ns["calibration_record"]
        self.assertEqual(retrieve(Backend(), {}, Job.creation_date)["status"], "unavailable")
        self.assertEqual(retrieve(self.backend, {}, None)["status"], "unavailable")
        self.assertEqual(self.backend.lookup_dates, [])
        self.ns["INCLUDE_BACKEND_PROPERTIES"] = False
        self.assertEqual(retrieve(self.backend, {}, Job.creation_date)["status"], "disabled")
        self.assertEqual(self.backend.lookup_dates, [])

    def test_failed_or_future_calibration_is_not_accepted(self):
        self.backend.snapshot["last_update_date"] = datetime(2026, 8, 1, tzinfo=timezone.utc)
        result = self.ns["retrieve_runtime_job"](Job(self.backend), "j")
        self.assertEqual(result["backend_calibration"]["status"], "failed")
        self.assertIsNone(result["backend_calibration"]["snapshot_id"])
        self.assertEqual(self.ns["calibration_snapshots"], {})
        self.assertEqual(result["backend_name"], "ibm_test")

    def test_physical_qubits_exclude_idle_width_and_barriers(self):
        circuit = QuantumCircuit(8, 1)
        circuit.x(2)
        circuit.cx(2, 5)
        circuit.barrier(7)
        circuit.measure(5, 0)
        with circuit.if_test((circuit.clbits[0], 1)):
            circuit.x(6)
        for pub in [(circuit,), SamplerPub.coerce(circuit)]:
            summary = self.ns["circuit_summary"](pub)
            self.assertEqual(summary["active_physical_qubits"], [2, 5, 6])
            self.assertEqual(summary["measured_physical_qubits"], [5])
            self.assertEqual(summary["circuit_width"], 8)

    def test_one_bad_circuit_does_not_discard_other_pub_metadata(self):
        circuit = QuantumCircuit(2)
        circuit.x(1)
        job = SimpleNamespace(inputs={"pubs": [(circuit,), ("undecoded",)], "options": {"shots": 100}})
        result = self.ns["input_summary"](job)
        self.assertEqual(result["pub_count"], 2)
        self.assertEqual(result["options"], {"shots": 100})
        self.assertEqual(result["circuits"][0]["summary"]["active_physical_qubits"], [1])
        self.assertIn("circuit_summary", result["circuits"][1]["errors"])

    def test_function_session_fallback_empty_and_failed_child_lookup(self):
        for raises in (False, True):
            with self.subTest(raises=raises):
                def children():
                    if raises:
                        raise RuntimeError("Child endpoint unavailable")
                    return []
                function = SimpleNamespace(
                    status=lambda: "DONE", raw_data={}, runtime_sessions=lambda: ["s1", "s2"],
                    runtime_jobs=children,
                )
                self.ns["catalog"] = SimpleNamespace(job=lambda jid: function)
                self.ns["catalog_auth_error"] = None
                calls = []
                self.ns["service"] = SimpleNamespace(
                    jobs=lambda **kwargs: [SimpleNamespace(job_id=lambda: "child")],
                    job=lambda jid: calls.append(jid) or Job(self.backend),
                )
                self.ns["runtime_record_cache"].clear()
                result = self.ns["retrieve_function_job"]("function")
                self.assertEqual(result["runtime_job_ids"], ["child"])
                self.assertEqual(calls, ["child"])
                self.assertEqual(result["child_discovery_status"], "recovered_from_sessions")
                self.assertEqual(result["runtime_jobs"][0]["backend_calibration"]["status"], "retrieved")

    def test_missing_function_children_are_partial(self):
        function = SimpleNamespace(
            status=lambda: "DONE", raw_data={}, runtime_sessions=lambda: [], runtime_jobs=lambda: [],
        )
        self.ns["catalog"] = SimpleNamespace(job=lambda jid: function)
        result = self.ns["retrieve_function_job"]("f")
        self.assertEqual(result["retrieval_status"], "partial")
        self.assertEqual(result["child_discovery_status"], "unavailable")

    def test_export_coverage_includes_children_and_strict_json(self):
        child = self.ns["retrieve_runtime_job"](Job(Backend()), "child")
        self.ns.update(
            runtime_record_cache={"child": child}, runtime_job_records=[], function_job_records=[],
            batch_records=[], RUNTIME_JOB_IDS=[], FUNCTION_JOB_IDS=[], BATCH_IDS=[],
            catalog_auth_error=None, SAVE_JSON=False, display=lambda value: None,
        )
        exec("".join(self.nb["cells"][10]["source"]), self.ns)
        payload = self.ns["retrieved_payload"]
        self.assertEqual(payload["summary"]["calibration_status_counts"], {"unavailable": 1})
        self.assertEqual(payload["summary"]["unique_runtime_job_count"], 1)
        json.dumps(payload, allow_nan=False)

    def test_batch_detail_failure_preserves_children_and_rerun_refreshes_cache(self):
        batch = SimpleNamespace(
            details=lambda: (_ for _ in ()).throw(RuntimeError("Details unavailable")),
            usage=lambda: 4,
        )
        self.ns.update(
            RUNTIME_JOB_IDS=[], FUNCTION_JOB_IDS=[], BATCH_IDS=["batch"],
            service=SimpleNamespace(
                jobs=lambda **kwargs: [SimpleNamespace(job_id=lambda: "child")],
                job=lambda jid: Job(self.backend),
            ),
        )
        # A previous failed lookup must be retried when the retrieval cell reruns.
        self.ns["runtime_record_cache"]["child"] = {"retrieval_status": "failed"}
        with patch("qiskit_ibm_runtime.Batch.from_id", return_value=batch):
            exec("".join(self.nb["cells"][8]["source"]), self.ns)
        result = self.ns["batch_records"][0]
        self.assertEqual(result["retrieval_status"], "partial")
        self.assertIn("details", result["field_errors"])
        self.assertEqual(result["usage_seconds"], 4)
        self.assertEqual(result["runtime_jobs"][0]["retrieval_status"], "retrieved")
        self.assertEqual(result["runtime_jobs"][0]["backend_calibration"]["status"], "retrieved")

    def test_code_has_no_workload_submission_or_wait_calls(self):
        forbidden = {"run", "submit", "result", "save_account", "wait_for_final_state"}
        for cell in self.nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            tree = ast.parse("".join(cell["source"]))
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    self.assertNotIn(node.func.attr, forbidden)


if __name__ == "__main__":
    unittest.main()
