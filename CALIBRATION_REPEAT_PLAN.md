# Calibration-window repeat plan

## Scope

Repeat a fixed representative subset across **2–3 distinct calibration windows**. These are close copies of the original notebooks, not a new execution framework. Keep the original circuits, authentication, transpilation policy, provider options/order, scoring, and JSON/CSV formats. Use the existing metadata-enrichment notebook afterward.

## Proposed subset and budget review

| Track | Conditions | Provider arms |
| --- | --- | --- |
| Sampler | BV-50, QPE-20, GHZ-50, RND-50 (depth 4) | IBM raw, IBM measurement twirling, Q-CTRL |
| Estimator | TFIM-50, 8 layers, full-chain observables | IBM raw, IBM TREX + twirling, Q-CTRL, QESEM |

This covers every circuit family at intermediate widths. Keep the original backend, requested 32,768 shots, seeds, TFIM angles, QESEM precision 0.1 and execution-time option 600 seconds. ZNE stays disabled. The source does not fix the transpiler seed; preserving its policy does not isolate calibration effects from compilation variability.

Sampler groups by width as before: six parent submissions per window (two widths × three providers). Estimator adds four. **One run of the subset in each of 2–3 windows means 20–30 parent submissions.** Functions can create additional child jobs; these counts are not QPU-time/cost estimates or a total spending cap.

Run the subset once per window, with no additional within-window repetitions. This measures variation across windows, not within-window variability separately. No loop automatically runs additional windows.

## Minimal changes

- `repeat_calibration_sampler.ipynb` copies `benchmark-FULLCHAIN_-_SAMPLER_JOBID_WORKFLOW_RND_nonzero_fixed.ipynb`.
- `repeat_calibration_estimator.ipynb` copies `benchmark-FULLCHAIN_-_ESTIMATOR.ipynb`.
- Original cell order, execution loops and results format are retained. Only the subset, output paths, introductory notes and submission guards change. Estimator also initializes `tfim_rows = []`, which was commented out in the source.
- Saved cell outputs are cleared. Sampler cache rebuilding defaults to False for collection; its original submission code still builds the cache.
- Results go to `results/calibration_repeats/<WINDOW_ID>/<track>/`. Existing results are untouched.
- No new calibration audit, provider-order rotation, result schema, scheduler or automatic recovery.

## Manual execution

1. Review the subset, settings and provider access with the professor before submitting. Authentication remains as in the source notebooks.
2. Set matching `WINDOW_ID="w01"` in both copies. Keep settings/labels unchanged when collecting the same jobs.
3. Sampler: explicitly enable submission with collection disabled. Collect later through the original manifest/cache workflow, with submission disabled and cache rebuilding disabled.
4. Estimator: explicitly set `RUN_EXPERIMENTS=True` and run the original synchronous execution cell. It waits for results and saves them as before.
5. Both create an exclusive `.submission_started` marker before submission. A second submission to that destination stops. After an error/interruption, reconcile the manifest, saved results and IBM account before retrying. Do not blindly remove the marker or change labels to bypass it. This is a safety stop, not an automatic resume mechanism.
6. After an observed calibration update on the same backend, manually select `w02`, then `w03` if approved. Keep provider comparisons close in time as practical. No later run starts automatically.
7. Enrich the saved IDs separately using `retrieve_ibm_job_metadata.ipynb`. Retain original raw outputs unchanged alongside the enrichment.

## Window verification and later analysis

A different day, label or Batch ID is not proof of a distinct calibration window. Use execution timestamps and available historical backend calibration evidence, including vendor Runtime children where accessible, to establish which calibrations applied. Queue delays can split a planned block. Missing/mixed evidence stays explicitly unverified; never count labels alone as verified windows. Enrichment may not expose all vendor internals.

Report individual condition/provider scores and paired differences by verified window: Sampler exact/valid-set success and TFIM MX/ZZ absolute error against the original MPS reference. Retain MZ in raw outputs for compatibility. Do not treat shots, PUBs, observables or vendor children as independent repetitions, or count shared job time once per observable. Show across-window variation separately from shot uncertainty. Report failures and missing data; do not select replacement runs because of favorable scores.

This addresses repeatability of selected fixed instances, not generalization across circuit instances, a compilation ablation, or resource normalization. Those remain separate revision tasks.
