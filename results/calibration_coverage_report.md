# Calibration evidence for the existing experiments

Source: `ibm_enriched_jobs/index.json` and the linked metadata, calibration snapshots and experiment JSONs. This is an offline analysis; no IBM retrieval or quantum execution was performed.

Enrichment retrieved at: 2026-09-08T01:42:39.770528+00:00. Original export SHA-256: `0f2d5eb87ee743c0142a6e896d84876b7580017688f10089b1b5a041cddf9dba`.

## What is counted

- A distinct calibration snapshot is a different stored snapshot hash at an actual Runtime execution-start timestamp, with its backend and last-update timestamp retained. All covered jobs here use `ibm_pittsburgh`; the 40 hashes also have 40 distinct last-update timestamps.
- Reported metrics/benchmark snapshots are not a complete log of physical recalibration events. These counts do not prove full-device recalibrations or changes on the particular qubits used.
- Each covered Runtime job has only an execution-start snapshot. No end-of-execution snapshot was retrieved, so the number of recalibrations *during* a job and stability throughout execution cannot be determined.
- Function jobs inherit evidence only from their discoverable Runtime children. Missing children or failed retrievals mean unknown evidence, not zero calibrations.
- Shared Sampler PUBs and TFIM observables do not count as independent jobs. Condition tables show unions of snapshots across providers, not repeated executions of the same provider/condition.
- Datasets remain separated by original results folder to avoid mixing different TFIM settings or RND variants. Conditions use saved algorithm/width fields; no cross-folder equivalence is assumed. Original files without job IDs cannot be assigned evidence.

## Coverage by experiment set

| Experiment set | Parent jobs | With start snapshot | Unknown | Distinct start snapshots |
| --- | ---: | ---: | ---: | ---: |
| ghz_parity | 10 | 8 | 2 | 6 |
| sampler_benchmark | 20 | 8 | 12 | 7 |
| sampler_benchmark-QCTRL | 7 | 7 | 0 | 3 |
| sampler_benchmark-QCTRL-RND | 12 | 12 | 0 | 4 |
| tfim_probe | 12 | 9 | 3 | 5 |
| tfim_probe-10K-8sites | 36 | 27 | 9 | 14 |
| tfim_probe-16layers-full-chain | 17 | 15 | 2 | 1 |

**Overall:** 114 parent jobs, 86 with execution-start evidence, 28 unknown, and 40 distinct snapshots, deduplicated globally. Of 98 unique Runtime records, 86 have snapshots and 12 failed retrieval. The other 16 unknown parent jobs are QESEM Functions without discoverable children. Each of the 86 covered parent jobs maps to one observed start snapshot; this does not imply one calibration throughout the job.

The index lists 11 additional original JSON files without job IDs; they are outside the 114 matched experiments and cannot be assigned calibration evidence.

## Per-condition evidence

A condition below means algorithm + width within the named experiment set. C01–C40 refer to the timestamp table below. Snapshot counts combine available provider evidence; unknown providers remain explicit.

### ghz_parity

| Condition | Parent jobs | Distinct snapshots | Snapshot labels | Unknown provider jobs |
| --- | ---: | ---: | --- | --- |
| GHZ parity, n=20 | 3 | 2 | C01, C02 | QESEM: 1 |
| GHZ parity, n=40 | 3 | 1 | C03 | QESEM: 1 |
| GHZ parity, n=60 | 2 | 2 | C04, C05 | None |
| GHZ parity, n=80 | 2 | 2 | C05, C06 | None |

### sampler_benchmark

| Condition | Parent jobs | Distinct snapshots | Snapshot labels | Unknown provider jobs |
| --- | ---: | ---: | --- | --- |
| BV, n=25 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| BV, n=50 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| BV, n=75 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| GHZ, n=25 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| GHZ, n=50 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| GHZ, n=75 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| GHZ, n=100 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| QPE, n=5 | 3 | 3 | C27, C28, C29 | None |
| QPE, n=10 | 3 | 3 | C30, C31, C32 | None |
| QPE, n=15 | 2 | 1 | C33 | None |
| QPE, n=20 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| QPE, n=30 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| RND, n=20 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |
| RND, n=30 | 2 | 0 | Unknown | IBM measurement twirling: 1, IBM raw: 1 |

### sampler_benchmark-QCTRL

| Condition | Parent jobs | Distinct snapshots | Snapshot labels | Unknown provider jobs |
| --- | ---: | ---: | --- | --- |
| BV, n=25 | 1 | 1 | C34 | None |
| BV, n=50 | 1 | 1 | C36 | None |
| BV, n=75 | 1 | 1 | C36 | None |
| GHZ, n=25 | 1 | 1 | C34 | None |
| GHZ, n=50 | 1 | 1 | C36 | None |
| GHZ, n=75 | 1 | 1 | C36 | None |
| GHZ, n=100 | 1 | 1 | C36 | None |
| QPE, n=10 | 1 | 1 | C34 | None |
| QPE, n=20 | 1 | 1 | C34 | None |
| QPE, n=30 | 1 | 1 | C35 | None |

### sampler_benchmark-QCTRL-RND

| Condition | Parent jobs | Distinct snapshots | Snapshot labels | Unknown provider jobs |
| --- | ---: | ---: | --- | --- |
| RND, n=25 | 3 | 2 | C37, C38 | None |
| RND, n=50 | 3 | 2 | C37, C38 | None |
| RND, n=75 | 3 | 2 | C37, C39 | None |
| RND, n=100 | 3 | 2 | C37, C40 | None |

### tfim_probe

| Condition | Parent jobs | Distinct snapshots | Snapshot labels | Unknown provider jobs |
| --- | ---: | ---: | --- | --- |
| TFIM, n=25 | 4 | 1 | C22 | QESEM: 1 |
| TFIM, n=50 | 4 | 3 | C22, C23, C24 | QESEM: 1 |
| TFIM, n=75 | 4 | 2 | C25, C26 | QESEM: 1 |

### tfim_probe-10K-8sites

| Condition | Parent jobs | Distinct snapshots | Snapshot labels | Unknown provider jobs |
| --- | ---: | ---: | --- | --- |
| TFIM, n=20 | 4 | 2 | C07, C08 | QESEM: 1 |
| TFIM, n=40 | 4 | 1 | C09 | QESEM: 1 |
| TFIM, n=60 | 4 | 1 | C10 | QESEM: 1 |
| TFIM, n=80 | 4 | 2 | C11, C12 | QESEM: 1 |
| TFIM, n=100 | 4 | 1 | C13 | QESEM: 1 |
| TFIM, n=120 | 4 | 2 | C14, C15 | QESEM: 1 |
| TFIM, n=130 | 4 | 1 | C16 | QESEM: 1 |
| TFIM, n=140 | 4 | 3 | C17, C18, C19 | QESEM: 1 |
| TFIM, n=150 | 4 | 1 | C20 | QESEM: 1 |

### tfim_probe-16layers-full-chain

| Condition | Parent jobs | Distinct snapshots | Snapshot labels | Unknown provider jobs |
| --- | ---: | ---: | --- | --- |
| TFIM, n=25 | 4 | 1 | C21 | QESEM: 1 |
| TFIM, n=50 | 4 | 1 | C21 | QESEM: 1 |
| TFIM, n=75 | 3 | 1 | C21 | None |
| TFIM, n=100 | 3 | 1 | C21 | None |
| TFIM, n=125 | 3 | 1 | C21 | None |

## Calibration snapshot timestamps (UTC)

| Label | Backend | Snapshot last updated | Snapshot file |
| --- | --- | --- | --- |
| C01 | ibm_pittsburgh | 2026-06-20T02:21:19+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/721b52c2c626268191eb93f8a373b64cf6287c638ee9702acc304d003bee3972.json) |
| C02 | ibm_pittsburgh | 2026-06-20T03:53:03+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/bb2afab02cbceba6b1b82df45f22011ac753c5056e21ccac01f8cfd74dfadebb.json) |
| C03 | ibm_pittsburgh | 2026-06-20T09:30:21+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/3e5b49c6f0d13ecd47d841db9efaf2e0f6fff46802a414e651fa2884601de6de.json) |
| C04 | ibm_pittsburgh | 2026-06-20T19:16:53+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/d7f0eb4e85c8ebe01f18789de2766d87c3ff952aa29a9bb2eff6a64ea90a5007.json) |
| C05 | ibm_pittsburgh | 2026-06-20T22:08:44+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/e2a743f9485cfc550eb6fb400be8fa6c8c034fddefe074bcc30342758cc1ccc6.json) |
| C06 | ibm_pittsburgh | 2026-06-20T23:36:41+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/03d4e89f65c96cb9bb6dd10ffd4a35b721ca46284e4980be55ab143e89b08313.json) |
| C07 | ibm_pittsburgh | 2026-06-21T19:52:38+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/3bfb554df54257a29afa16d07449cbe033eba571a37a821fe918053a63162e50.json) |
| C08 | ibm_pittsburgh | 2026-06-21T21:16:40+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/63a9b5f78e427606c8bd3587e7982a869d17aa270ed9e8f61d9073cccbcd754b.json) |
| C09 | ibm_pittsburgh | 2026-06-22T06:15:37+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/d360204b79c43439b98eafbb8228a1115e9e96e31500cd00889355cc003054fa.json) |
| C10 | ibm_pittsburgh | 2026-06-22T07:49:24+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/84fe10067095bc666a95aae93d219d4e5320485ebcf56430c0d8c015b5c0850f.json) |
| C11 | ibm_pittsburgh | 2026-06-22T09:03:14+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/5d7278a601c6302fee8da9d7330c62c6da935b5d456c9a7a2bc5bb13ddf0c0c1.json) |
| C12 | ibm_pittsburgh | 2026-06-22T09:15:52+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/321dd109738fc0d12c30dfa86f9554f93c096bafc8828583e7c69c9a1d710c99.json) |
| C13 | ibm_pittsburgh | 2026-06-22T14:59:28+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/7f3308e5c0f9d6369a8d2e23716b454dde8ec0da5cee6d3dda76ca7962783030.json) |
| C14 | ibm_pittsburgh | 2026-06-23T05:05:25+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/0bb07e7458ec7abfa020ec1e6e142982cc94e917b6e67616a9b0d248c5251d40.json) |
| C15 | ibm_pittsburgh | 2026-06-23T06:26:01+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/eb80901eb154c1e57a7ca281205bbe2daf48199443da0f443e5661c148089e1f.json) |
| C16 | ibm_pittsburgh | 2026-06-24T12:49:27+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/19db82f7a8adfa31202efdaefe7d89e818bd0ef65898787b7032207e1530623d.json) |
| C17 | ibm_pittsburgh | 2026-06-24T14:32:05+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/dead1acaca2d42001521bf4091a4402fcef487bd158025cfaa721e5020ef888c.json) |
| C18 | ibm_pittsburgh | 2026-06-24T17:15:53+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/fd9c351faf5028ea0585d5e69fc2c34832aa39d9f3fa398f556aad993e984eca.json) |
| C19 | ibm_pittsburgh | 2026-06-24T18:36:09+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/42169eaf4f53928740645563db8922783a391b6d0b8a99085e62a348e61091d3.json) |
| C20 | ibm_pittsburgh | 2026-06-24T21:27:19+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/42473210ca1f00f21a86e1c4e816e30d051043f828e00c64722c264fd459e1b7.json) |
| C21 | ibm_pittsburgh | 2026-06-27T01:45:20+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/834118360f58c45a5b87b55d29a01054b9df2c341a65bdc4bf40f54a1d7fad16.json) |
| C22 | ibm_pittsburgh | 2026-06-30T01:35:50+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/f15eeb94a2da46e4061ad69b07ba045cc57a285ba12f8cff020c1926dde08592.json) |
| C23 | ibm_pittsburgh | 2026-06-30T02:39:59+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/3958247e824bbfdeebc6bea829fe31330873edf824c0a3c32c05f49fb31d1f08.json) |
| C24 | ibm_pittsburgh | 2026-06-30T05:40:17+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/6aebe87f861ce2247e3ad511ea8ecfcdafa39ce351dd280f6203cfc45b346c6e.json) |
| C25 | ibm_pittsburgh | 2026-06-30T18:55:46+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/e513cd4fd6b1393bf8f775b825c3827026ec28b76a7614d0a7d2fb384d6de05b.json) |
| C26 | ibm_pittsburgh | 2026-07-01T03:43:10+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/f79464de1d8050f273bbad1004e8568779461f956e31bdab564a384c7ab7b65e.json) |
| C27 | ibm_pittsburgh | 2026-07-08T16:31:09+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/53956d65a1680c89a4b53a9333db0154b01ae714a207686eba537a18214a99c1.json) |
| C28 | ibm_pittsburgh | 2026-07-08T17:57:35+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/fc422326bebd1a6545c5ccfcba8bf31447276a69f0a20a53b6fcefef11658893.json) |
| C29 | ibm_pittsburgh | 2026-07-08T19:17:45+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/935f4ea301723ac6771b15a87355be5afb5272c708647a4b54fa30adea52ed75.json) |
| C30 | ibm_pittsburgh | 2026-07-08T20:41:33+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/e2350203a30715b32981132684c360e7cf90981878915edf9441025fe4fabdc6.json) |
| C31 | ibm_pittsburgh | 2026-07-08T22:02:33+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/fa851462c5d6030d371930e40d14f873c43282f18506989a261b7ee0cd5d004f.json) |
| C32 | ibm_pittsburgh | 2026-07-08T23:15:15+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/eba25440081e639419ec87915f47bd65142bae44c7539652230c674b4031cc38.json) |
| C33 | ibm_pittsburgh | 2026-07-09T00:48:39+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/56d7a0ff3845a2060dc889fd43911d87d7d9a9ca40cd59e38cb85b5435fcaf4c.json) |
| C34 | ibm_pittsburgh | 2026-07-10T00:59:35+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/101a0a78908fc3bcc97bfea86cfe39af44eed5e14ec1cc4d7fb353fc5c92e239.json) |
| C35 | ibm_pittsburgh | 2026-07-10T16:47:43+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/88ab6aa6fd8289d8f2b795ef907daa202dbdfda60aa3a43ca6613f8575942479.json) |
| C36 | ibm_pittsburgh | 2026-07-10T18:13:11+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/d32557497c0ac73cf60a9daf2f3f9d70148c49202dbc973c01d84bf0d8a1d827.json) |
| C37 | ibm_pittsburgh | 2026-07-12T20:57:08+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/41e99d03ad31cf85966e35d13d582d3585d23f77e8d2d91efed0bba8c9ae81c8.json) |
| C38 | ibm_pittsburgh | 2026-07-13T05:59:27+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/6a34de6b1cb3b3f099d55d442f687c9c4d6ff0ec4b0915683b986312ca3e82cb.json) |
| C39 | ibm_pittsburgh | 2026-07-13T08:35:24+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/76832055f59d8c381d115b34955f62f2dcfb51324247d858086031c096b9bf0d.json) |
| C40 | ibm_pittsburgh | 2026-07-13T10:07:48+00:00 | [JSON](ibm_enriched_jobs/calibration_snapshots/8f7b2440dd4ef335928027da04eb9ec959a7d60195010740bd220d74af91532f.json) |

## Every matched experiment job

Execution timestamps are UTC. The snapshot timestamp is its last update, not the experiment time. For Functions, the displayed execution range comes from available Runtime children only. Raw source files retain shots, options, circuit metadata and scoring information where recorded.

### ghz_parity

| Provider | Conditions | Job metadata | Execution start (UTC) | Snapshot | Original experiment copy |
| --- | --- | --- | --- | --- | --- |
| IBM default | GHZ parity n=20 | [d8qvms6gbcrc73f3v89g](ibm_enriched_jobs/jobs/d8qvms6gbcrc73f3v89g/metadata.json) | 2026-06-20T03:04:06.771775+00:00 | C01 | [JSON](ibm_enriched_jobs/jobs/d8qvms6gbcrc73f3v89g/experiments/ghz_parity/IBM_DEFAULT_GHZ_n20.json) |
| Q-CTRL | GHZ parity n=20 | [e58d4f4a-0560-4438-ad2c-407532b445fa](ibm_enriched_jobs/jobs/e58d4f4a-0560-4438-ad2c-407532b445fa/metadata.json) | 2026-06-20T04:17:44.327928+00:00 | C02 | [JSON](ibm_enriched_jobs/jobs/e58d4f4a-0560-4438-ad2c-407532b445fa/experiments/ghz_parity/QCTRL_GHZ_n20.json) |
| QESEM | GHZ parity n=20 | [df40092a-7e1c-41ab-9a52-db53914c9c70](ibm_enriched_jobs/jobs/df40092a-7e1c-41ab-9a52-db53914c9c70/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/df40092a-7e1c-41ab-9a52-db53914c9c70/experiments/ghz_parity/QESEM_GHZ_n20.json) |
| IBM default | GHZ parity n=40 | [d8r53deab0ds73dr8phg](ibm_enriched_jobs/jobs/d8r53deab0ds73dr8phg/metadata.json) | 2026-06-20T10:13:31.830636+00:00 | C03 | [JSON](ibm_enriched_jobs/jobs/d8r53deab0ds73dr8phg/experiments/ghz_parity/IBM_DEFAULT_GHZ_n40.json) |
| Q-CTRL | GHZ parity n=40 | [2d258c03-4265-4ee9-b1a8-b974a14e047e](ibm_enriched_jobs/jobs/2d258c03-4265-4ee9-b1a8-b974a14e047e/metadata.json) | 2026-06-20T10:34:35.758536+00:00 | C03 | [JSON](ibm_enriched_jobs/jobs/2d258c03-4265-4ee9-b1a8-b974a14e047e/experiments/ghz_parity/QCTRL_GHZ_n40.json) |
| QESEM | GHZ parity n=40 | [518b77c3-3b69-4c60-b390-9308f132a927](ibm_enriched_jobs/jobs/518b77c3-3b69-4c60-b390-9308f132a927/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/518b77c3-3b69-4c60-b390-9308f132a927/experiments/ghz_parity/QESEM_GHZ_n40.json) |
| IBM default | GHZ parity n=60 | [d8rf4dmab0ds73drk25g](ibm_enriched_jobs/jobs/d8rf4dmab0ds73drk25g/metadata.json) | 2026-06-20T20:45:57.007312+00:00 | C04 | [JSON](ibm_enriched_jobs/jobs/d8rf4dmab0ds73drk25g/experiments/ghz_parity/IBM_DEFAULT_GHZ_n60.json) |
| Q-CTRL | GHZ parity n=60 | [db75adbd-1537-4e7b-8d57-1e6839d2c08f](ibm_enriched_jobs/jobs/db75adbd-1537-4e7b-8d57-1e6839d2c08f/metadata.json) | 2026-06-20T22:26:21.563858+00:00 | C05 | [JSON](ibm_enriched_jobs/jobs/db75adbd-1537-4e7b-8d57-1e6839d2c08f/experiments/ghz_parity/QCTRL_GHZ_n60.json) |
| IBM default | GHZ parity n=80 | [d8ri28i01fac73d4c7v0](ibm_enriched_jobs/jobs/d8ri28i01fac73d4c7v0/metadata.json) | 2026-06-20T23:48:38.300984+00:00 | C05 | [JSON](ibm_enriched_jobs/jobs/d8ri28i01fac73d4c7v0/experiments/ghz_parity/IBM_DEFAULT_GHZ_n80.json) |
| Q-CTRL | GHZ parity n=80 | [3adfcd16-fe3a-4c8a-a36d-57bbb66ef6eb](ibm_enriched_jobs/jobs/3adfcd16-fe3a-4c8a-a36d-57bbb66ef6eb/metadata.json) | 2026-06-21T00:30:25.728191+00:00 | C06 | [JSON](ibm_enriched_jobs/jobs/3adfcd16-fe3a-4c8a-a36d-57bbb66ef6eb/experiments/ghz_parity/QCTRL_GHZ_n80.json) |

### sampler_benchmark

| Provider | Conditions | Job metadata | Execution start (UTC) | Snapshot | Original experiment copy |
| --- | --- | --- | --- | --- | --- |
| IBM measurement twirling | BV n=25, GHZ n=25 | [d96rhjgtcv6s73dk4if0](ibm_enriched_jobs/jobs/d96rhjgtcv6s73dk4if0/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96rhjgtcv6s73dk4if0/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n25.json) |
| IBM raw | BV n=25, GHZ n=25 | [d96r6u4qp3as739qukng](ibm_enriched_jobs/jobs/d96r6u4qp3as739qukng/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96r6u4qp3as739qukng/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n25.json) |
| IBM measurement twirling | BV n=50, GHZ n=50 | [d96thj8tcv6s73dk6o7g](ibm_enriched_jobs/jobs/d96thj8tcv6s73dk6o7g/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96thj8tcv6s73dk6o7g/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n50.json) |
| IBM raw | BV n=50, GHZ n=50 | [d96stogtcv6s73dk60h0](ibm_enriched_jobs/jobs/d96stogtcv6s73dk60h0/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96stogtcv6s73dk60h0/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n50.json) |
| IBM measurement twirling | BV n=75, GHZ n=75 | [d96uof0tcv6s73dk88hg](ibm_enriched_jobs/jobs/d96uof0tcv6s73dk88hg/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96uof0tcv6s73dk88hg/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n75.json) |
| IBM raw | BV n=75, GHZ n=75 | [d96tkft2su3c739hcac0](ibm_enriched_jobs/jobs/d96tkft2su3c739hcac0/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96tkft2su3c739hcac0/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n75.json) |
| IBM measurement twirling | GHZ n=100 | [d96vk7sqp3as739r3t1g](ibm_enriched_jobs/jobs/d96vk7sqp3as739r3t1g/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96vk7sqp3as739r3t1g/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n100.json) |
| IBM raw | GHZ n=100 | [d96v222f47jc73a62o8g](ibm_enriched_jobs/jobs/d96v222f47jc73a62o8g/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96v222f47jc73a62o8g/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n100.json) |
| IBM measurement twirling | QPE n=5 | [d979bokqp3as739rg9fg](ibm_enriched_jobs/jobs/d979bokqp3as739rg9fg/metadata.json) | 2026-07-08T18:24:35.669826+00:00 | C28 | [JSON](ibm_enriched_jobs/jobs/d979bokqp3as739rg9fg/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n5.json) |
| IBM raw | QPE n=5 | [d978e4kqp3as739rf8pg](ibm_enriched_jobs/jobs/d978e4kqp3as739rf8pg/metadata.json) | 2026-07-08T17:45:47.942437+00:00 | C27 | [JSON](ibm_enriched_jobs/jobs/d978e4kqp3as739rf8pg/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n5.json) |
| Q-CTRL | QPE n=5 | [b9357e1e-e7dc-4f0d-97c9-b05adf10e708](ibm_enriched_jobs/jobs/b9357e1e-e7dc-4f0d-97c9-b05adf10e708/metadata.json) | 2026-07-08T20:42:22.807932+00:00 | C29 | [JSON](ibm_enriched_jobs/jobs/b9357e1e-e7dc-4f0d-97c9-b05adf10e708/experiments/sampler_benchmark/Q_CTRL_SAMPLER_n5.json) |
| IBM measurement twirling | QPE n=10 | [d97cvqd2su3c739hvcf0](ibm_enriched_jobs/jobs/d97cvqd2su3c739hvcf0/metadata.json) | 2026-07-08T22:32:11.290615+00:00 | C31 | [JSON](ibm_enriched_jobs/jobs/d97cvqd2su3c739hvcf0/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n10.json) |
| IBM raw | QPE n=10 | [d97bctif47jc73a6i6h0](ibm_enriched_jobs/jobs/d97bctif47jc73a6i6h0/metadata.json) | 2026-07-08T22:11:00.968493+00:00 | C30 | [JSON](ibm_enriched_jobs/jobs/d97bctif47jc73a6i6h0/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n10.json) |
| Q-CTRL | QPE n=10 | [f0d2caaa-0d95-4472-9d7f-68267d777720](ibm_enriched_jobs/jobs/f0d2caaa-0d95-4472-9d7f-68267d777720/metadata.json) | 2026-07-08T23:35:22.766663+00:00 | C32 | [JSON](ibm_enriched_jobs/jobs/f0d2caaa-0d95-4472-9d7f-68267d777720/experiments/sampler_benchmark/Q_CTRL_SAMPLER_n10.json) |
| IBM measurement twirling | QPE n=15 | [d97f5iaf47jc73a6m8a0](ibm_enriched_jobs/jobs/d97f5iaf47jc73a6m8a0/metadata.json) | 2026-07-09T01:20:28.043733+00:00 | C33 | [JSON](ibm_enriched_jobs/jobs/d97f5iaf47jc73a6m8a0/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n15.json) |
| IBM raw | QPE n=15 | [d97eh3if47jc73a6lhcg](ibm_enriched_jobs/jobs/d97eh3if47jc73a6lhcg/metadata.json) | 2026-07-09T01:00:34.232404+00:00 | C33 | [JSON](ibm_enriched_jobs/jobs/d97eh3if47jc73a6lhcg/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n15.json) |
| IBM measurement twirling | QPE n=20, RND n=20 | [d96ql9if47jc73a5tqtg](ibm_enriched_jobs/jobs/d96ql9if47jc73a5tqtg/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96ql9if47jc73a5tqtg/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n20.json) |
| IBM raw | QPE n=20, RND n=20 | [d96qk44qp3as739qu2mg](ibm_enriched_jobs/jobs/d96qk44qp3as739qu2mg/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96qk44qp3as739qu2mg/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n20.json) |
| IBM measurement twirling | QPE n=30, RND n=30 | [d96rta4qp3as739qvb6g](ibm_enriched_jobs/jobs/d96rta4qp3as739qvb6g/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96rta4qp3as739qvb6g/experiments/sampler_benchmark/IBM_MEASUREMENT_TWIRLING_SAMPLER_n30.json) |
| IBM raw | QPE n=30, RND n=30 | [d96rsj4qp3as739qvabg](ibm_enriched_jobs/jobs/d96rsj4qp3as739qvabg/metadata.json) | Unavailable | Unknown: failed / calibration unavailable | [JSON](ibm_enriched_jobs/jobs/d96rsj4qp3as739qvabg/experiments/sampler_benchmark/IBM_RAW_SAMPLER_n30.json) |

### sampler_benchmark-QCTRL

| Provider | Conditions | Job metadata | Execution start (UTC) | Snapshot | Original experiment copy |
| --- | --- | --- | --- | --- | --- |
| Q-CTRL | BV n=25, GHZ n=25 | [60ac4581-8b74-4078-a6b9-1708efd15b40](ibm_enriched_jobs/jobs/60ac4581-8b74-4078-a6b9-1708efd15b40/metadata.json) | 2026-07-10T01:19:04.974710+00:00 | C34 | [JSON](ibm_enriched_jobs/jobs/60ac4581-8b74-4078-a6b9-1708efd15b40/experiments/sampler_benchmark-QCTRL/Q_CTRL_SAMPLER_n25.json) |
| Q-CTRL | BV n=50, GHZ n=50 | [26c2dee4-b8ba-4be9-933b-b74c43d772de](ibm_enriched_jobs/jobs/26c2dee4-b8ba-4be9-933b-b74c43d772de/metadata.json) | 2026-07-10T18:37:03.443683+00:00 | C36 | [JSON](ibm_enriched_jobs/jobs/26c2dee4-b8ba-4be9-933b-b74c43d772de/experiments/sampler_benchmark-QCTRL/Q_CTRL_SAMPLER_n50.json) |
| Q-CTRL | BV n=75, GHZ n=75 | [7472b14f-7ccf-40a3-9aa6-560f2e9be570](ibm_enriched_jobs/jobs/7472b14f-7ccf-40a3-9aa6-560f2e9be570/metadata.json) | 2026-07-10T19:21:26.715876+00:00 | C36 | [JSON](ibm_enriched_jobs/jobs/7472b14f-7ccf-40a3-9aa6-560f2e9be570/experiments/sampler_benchmark-QCTRL/Q_CTRL_SAMPLER_n75.json) |
| Q-CTRL | GHZ n=100 | [6e5c0afc-7d48-4e77-9ab1-537cb790e9fd](ibm_enriched_jobs/jobs/6e5c0afc-7d48-4e77-9ab1-537cb790e9fd/metadata.json) | 2026-07-10T19:49:54.156451+00:00 | C36 | [JSON](ibm_enriched_jobs/jobs/6e5c0afc-7d48-4e77-9ab1-537cb790e9fd/experiments/sampler_benchmark-QCTRL/Q_CTRL_SAMPLER_n100.json) |
| Q-CTRL | QPE n=10 | [2fa397f9-140d-4d70-a69c-f71cd0cb7983](ibm_enriched_jobs/jobs/2fa397f9-140d-4d70-a69c-f71cd0cb7983/metadata.json) | 2026-07-10T01:18:37.965434+00:00 | C34 | [JSON](ibm_enriched_jobs/jobs/2fa397f9-140d-4d70-a69c-f71cd0cb7983/experiments/sampler_benchmark-QCTRL/Q_CTRL_SAMPLER_n10.json) |
| Q-CTRL | QPE n=20 | [c656f3ae-368d-49c1-b2cb-d240e15d9cd3](ibm_enriched_jobs/jobs/c656f3ae-368d-49c1-b2cb-d240e15d9cd3/metadata.json) | 2026-07-10T01:19:03.542407+00:00 | C34 | [JSON](ibm_enriched_jobs/jobs/c656f3ae-368d-49c1-b2cb-d240e15d9cd3/experiments/sampler_benchmark-QCTRL/Q_CTRL_SAMPLER_n20.json) |
| Q-CTRL | QPE n=30 | [4b3e4ab5-0f54-4522-a303-2e51f8af178e](ibm_enriched_jobs/jobs/4b3e4ab5-0f54-4522-a303-2e51f8af178e/metadata.json) | 2026-07-10T18:01:03.499719+00:00 | C35 | [JSON](ibm_enriched_jobs/jobs/4b3e4ab5-0f54-4522-a303-2e51f8af178e/experiments/sampler_benchmark-QCTRL/Q_CTRL_SAMPLER_n30.json) |

### sampler_benchmark-QCTRL-RND

| Provider | Conditions | Job metadata | Execution start (UTC) | Snapshot | Original experiment copy |
| --- | --- | --- | --- | --- | --- |
| IBM measurement twirling | RND n=25 | [d9a030l2su3c739l0asg](ibm_enriched_jobs/jobs/d9a030l2su3c739l0asg/metadata.json) | 2026-07-12T21:40:31.063597+00:00 | C37 | [JSON](ibm_enriched_jobs/jobs/d9a030l2su3c739l0asg/experiments/sampler_benchmark-QCTRL-RND/IBM_MEASUREMENT_TWIRLING_SAMPLER_n25.json) |
| IBM raw | RND n=25 | [d9a030d2su3c739l0as0](ibm_enriched_jobs/jobs/d9a030d2su3c739l0as0/metadata.json) | 2026-07-12T21:39:54.363023+00:00 | C37 | [JSON](ibm_enriched_jobs/jobs/d9a030d2su3c739l0as0/experiments/sampler_benchmark-QCTRL-RND/IBM_RAW_SAMPLER_n25.json) |
| Q-CTRL | RND n=25 | [d5c8dff5-4fc2-4619-a484-b2230b152882](ibm_enriched_jobs/jobs/d5c8dff5-4fc2-4619-a484-b2230b152882/metadata.json) | 2026-07-13T07:38:54.422187+00:00 | C38 | [JSON](ibm_enriched_jobs/jobs/d5c8dff5-4fc2-4619-a484-b2230b152882/experiments/sampler_benchmark-QCTRL-RND/Q_CTRL_SAMPLER_n25.json) |
| IBM measurement twirling | RND n=50 | [d9a032otcv6s73dnru8g](ibm_enriched_jobs/jobs/d9a032otcv6s73dnru8g/metadata.json) | 2026-07-12T21:40:56.904280+00:00 | C37 | [JSON](ibm_enriched_jobs/jobs/d9a032otcv6s73dnru8g/experiments/sampler_benchmark-QCTRL-RND/IBM_MEASUREMENT_TWIRLING_SAMPLER_n50.json) |
| IBM raw | RND n=50 | [d9a032l2su3c739l0b00](ibm_enriched_jobs/jobs/d9a032l2su3c739l0b00/metadata.json) | 2026-07-12T21:40:45.455070+00:00 | C37 | [JSON](ibm_enriched_jobs/jobs/d9a032l2su3c739l0b00/experiments/sampler_benchmark-QCTRL-RND/IBM_RAW_SAMPLER_n50.json) |
| Q-CTRL | RND n=50 | [9a455734-b445-4984-bf1d-38788a2ed205](ibm_enriched_jobs/jobs/9a455734-b445-4984-bf1d-38788a2ed205/metadata.json) | 2026-07-13T08:50:09.983330+00:00 | C38 | [JSON](ibm_enriched_jobs/jobs/9a455734-b445-4984-bf1d-38788a2ed205/experiments/sampler_benchmark-QCTRL-RND/Q_CTRL_SAMPLER_n50.json) |
| IBM measurement twirling | RND n=75 | [d9a034d2su3c739l0b20](ibm_enriched_jobs/jobs/d9a034d2su3c739l0b20/metadata.json) | 2026-07-12T21:42:38.064865+00:00 | C37 | [JSON](ibm_enriched_jobs/jobs/d9a034d2su3c739l0b20/experiments/sampler_benchmark-QCTRL-RND/IBM_MEASUREMENT_TWIRLING_SAMPLER_n75.json) |
| IBM raw | RND n=75 | [d9a0348tcv6s73dnrua0](ibm_enriched_jobs/jobs/d9a0348tcv6s73dnrua0/metadata.json) | 2026-07-12T21:42:37.399672+00:00 | C37 | [JSON](ibm_enriched_jobs/jobs/d9a0348tcv6s73dnrua0/experiments/sampler_benchmark-QCTRL-RND/IBM_RAW_SAMPLER_n75.json) |
| Q-CTRL | RND n=75 | [08cce1b7-1caa-4c35-9fa6-a798bd361d08](ibm_enriched_jobs/jobs/08cce1b7-1caa-4c35-9fa6-a798bd361d08/metadata.json) | 2026-07-13T09:26:09.320970+00:00 | C39 | [JSON](ibm_enriched_jobs/jobs/08cce1b7-1caa-4c35-9fa6-a798bd361d08/experiments/sampler_benchmark-QCTRL-RND/Q_CTRL_SAMPLER_n75.json) |
| IBM measurement twirling | RND n=100 | [d9a036gtcv6s73dnrudg](ibm_enriched_jobs/jobs/d9a036gtcv6s73dnrudg/metadata.json) | 2026-07-12T21:43:19.938977+00:00 | C37 | [JSON](ibm_enriched_jobs/jobs/d9a036gtcv6s73dnrudg/experiments/sampler_benchmark-QCTRL-RND/IBM_MEASUREMENT_TWIRLING_SAMPLER_n100.json) |
| IBM raw | RND n=100 | [d9a036cqp3as739ulvd0](ibm_enriched_jobs/jobs/d9a036cqp3as739ulvd0/metadata.json) | 2026-07-12T21:42:58.675695+00:00 | C37 | [JSON](ibm_enriched_jobs/jobs/d9a036cqp3as739ulvd0/experiments/sampler_benchmark-QCTRL-RND/IBM_RAW_SAMPLER_n100.json) |
| Q-CTRL | RND n=100 | [f64d97a4-2a5e-41f5-8507-4a0f082b1430](ibm_enriched_jobs/jobs/f64d97a4-2a5e-41f5-8507-4a0f082b1430/metadata.json) | 2026-07-13T10:27:55.547076+00:00 | C40 | [JSON](ibm_enriched_jobs/jobs/f64d97a4-2a5e-41f5-8507-4a0f082b1430/experiments/sampler_benchmark-QCTRL-RND/Q_CTRL_SAMPLER_n100.json) |

### tfim_probe

| Provider | Conditions | Job metadata | Execution start (UTC) | Snapshot | Original experiment copy |
| --- | --- | --- | --- | --- | --- |
| IBM TREX + twirling | TFIM n=25 | [d91i5fnccmks73d56rbg](ibm_enriched_jobs/jobs/d91i5fnccmks73d56rbg/metadata.json) | 2026-06-30T01:58:50.913470+00:00 | C22 | [JSON](ibm_enriched_jobs/jobs/d91i5fnccmks73d56rbg/experiments/tfim_probe/IBM_TREX_TWIRLING_TFIM_n25.json) |
| IBM raw | TFIM n=25 | [d91h10j57qjs73b6bfng](ibm_enriched_jobs/jobs/d91h10j57qjs73b6bfng/metadata.json) | 2026-06-30T01:57:58.070356+00:00 | C22 | [JSON](ibm_enriched_jobs/jobs/d91h10j57qjs73b6bfng/experiments/tfim_probe/IBM_RAW_TFIM_n25.json) |
| Q-CTRL | TFIM n=25 | [2fd27b98-4cda-4fdb-b34a-392b568b25d9](ibm_enriched_jobs/jobs/2fd27b98-4cda-4fdb-b34a-392b568b25d9/metadata.json) | 2026-06-30T02:01:16.718862+00:00 | C22 | [JSON](ibm_enriched_jobs/jobs/2fd27b98-4cda-4fdb-b34a-392b568b25d9/experiments/tfim_probe/QCTRL_TFIM_n25.json) |
| QESEM | TFIM n=25 | [923a7c33-5eea-476b-9794-41da3a5aa471](ibm_enriched_jobs/jobs/923a7c33-5eea-476b-9794-41da3a5aa471/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/923a7c33-5eea-476b-9794-41da3a5aa471/experiments/tfim_probe/QESEM_TFIM_n25.json) |
| IBM TREX + twirling | TFIM n=50 | [d91issr57qjs73b6et40](ibm_enriched_jobs/jobs/d91issr57qjs73b6et40/metadata.json) | 2026-06-30T02:48:20.732595+00:00 | C23 | [JSON](ibm_enriched_jobs/jobs/d91issr57qjs73b6et40/experiments/tfim_probe/IBM_TREX_TWIRLING_TFIM_n50.json) |
| IBM raw | TFIM n=50 | [d91irt7qq29s738np1i0](ibm_enriched_jobs/jobs/d91irt7qq29s738np1i0/metadata.json) | 2026-06-30T02:46:15.863438+00:00 | C22 | [JSON](ibm_enriched_jobs/jobs/d91irt7qq29s738np1i0/experiments/tfim_probe/IBM_RAW_TFIM_n50.json) |
| Q-CTRL | TFIM n=50 | [16ea48d1-d9d6-403d-b399-adccc7d42997](ibm_enriched_jobs/jobs/16ea48d1-d9d6-403d-b399-adccc7d42997/metadata.json) | 2026-06-30T05:51:22.729036+00:00 | C24 | [JSON](ibm_enriched_jobs/jobs/16ea48d1-d9d6-403d-b399-adccc7d42997/experiments/tfim_probe/QCTRL_TFIM_n50.json) |
| QESEM | TFIM n=50 | [4b80b737-f982-4d36-ae9e-cc01ad870cb6](ibm_enriched_jobs/jobs/4b80b737-f982-4d36-ae9e-cc01ad870cb6/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/4b80b737-f982-4d36-ae9e-cc01ad870cb6/experiments/tfim_probe/QESEM_TFIM_n50.json) |
| IBM TREX + twirling | TFIM n=75 | [d921d3vqq29s738ohgqg](ibm_enriched_jobs/jobs/d921d3vqq29s738ohgqg/metadata.json) | 2026-07-01T06:02:52.223136+00:00 | C26 | [JSON](ibm_enriched_jobs/jobs/d921d3vqq29s738ohgqg/experiments/tfim_probe/IBM_TREX_TWIRLING_TFIM_n75.json) |
| IBM raw | TFIM n=75 | [d9213luu9n7c73aniku0](ibm_enriched_jobs/jobs/d9213luu9n7c73aniku0/metadata.json) | 2026-06-30T19:17:08.867485+00:00 | C25 | [JSON](ibm_enriched_jobs/jobs/d9213luu9n7c73aniku0/experiments/tfim_probe/IBM_RAW_TFIM_n75.json) |
| Q-CTRL | TFIM n=75 | [2414fb86-2f60-4d78-bfbb-a36c78d26914](ibm_enriched_jobs/jobs/2414fb86-2f60-4d78-bfbb-a36c78d26914/metadata.json) | 2026-07-01T06:10:33.146918+00:00 | C26 | [JSON](ibm_enriched_jobs/jobs/2414fb86-2f60-4d78-bfbb-a36c78d26914/experiments/tfim_probe/QCTRL_TFIM_n75.json) |
| QESEM | TFIM n=75 | [2a3f7475-37b2-4dbc-a3ec-01391a4c0c25](ibm_enriched_jobs/jobs/2a3f7475-37b2-4dbc-a3ec-01391a4c0c25/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/2a3f7475-37b2-4dbc-a3ec-01391a4c0c25/experiments/tfim_probe/QESEM_TFIM_n75.json) |

### tfim_probe-10K-8sites

| Provider | Conditions | Job metadata | Execution start (UTC) | Snapshot | Original experiment copy |
| --- | --- | --- | --- | --- | --- |
| IBM TREX + twirling | TFIM n=20 | [d8s4ova01fac73d51on0](ibm_enriched_jobs/jobs/d8s4ova01fac73d51on0/metadata.json) | 2026-06-21T20:41:34.814842+00:00 | C07 | [JSON](ibm_enriched_jobs/jobs/d8s4ova01fac73d51on0/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n20.json) |
| IBM raw | TFIM n=20 | [d8s47u6ab0ds73dsbq4g](ibm_enriched_jobs/jobs/d8s47u6ab0ds73dsbq4g/metadata.json) | 2026-06-21T20:29:57.492180+00:00 | C07 | [JSON](ibm_enriched_jobs/jobs/d8s47u6ab0ds73dsbq4g/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n20.json) |
| Q-CTRL | TFIM n=20 | [9b5a3e56-b669-48a9-bd7d-fbf1fcc8f450](ibm_enriched_jobs/jobs/9b5a3e56-b669-48a9-bd7d-fbf1fcc8f450/metadata.json) | 2026-06-21T22:12:42.607616+00:00 | C08 | [JSON](ibm_enriched_jobs/jobs/9b5a3e56-b669-48a9-bd7d-fbf1fcc8f450/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n20.json) |
| QESEM | TFIM n=20 | [3e465984-7894-4689-a472-2982872b9eac](ibm_enriched_jobs/jobs/3e465984-7894-4689-a472-2982872b9eac/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/3e465984-7894-4689-a472-2982872b9eac/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n20.json) |
| IBM TREX + twirling | TFIM n=40 | [d8sdopa01fac73d5ca8g](ibm_enriched_jobs/jobs/d8sdopa01fac73d5ca8g/metadata.json) | 2026-06-22T06:56:03.298196+00:00 | C09 | [JSON](ibm_enriched_jobs/jobs/d8sdopa01fac73d5ca8g/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n40.json) |
| IBM raw | TFIM n=40 | [d8sdbcmkodhs7385eahg](ibm_enriched_jobs/jobs/d8sdbcmkodhs7385eahg/metadata.json) | 2026-06-22T06:51:38.549206+00:00 | C09 | [JSON](ibm_enriched_jobs/jobs/d8sdbcmkodhs7385eahg/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n40.json) |
| Q-CTRL | TFIM n=40 | [7d2ed44f-6934-4326-8087-e58d95cdf600](ibm_enriched_jobs/jobs/7d2ed44f-6934-4326-8087-e58d95cdf600/metadata.json) | 2026-06-22T07:00:57.874141+00:00 | C09 | [JSON](ibm_enriched_jobs/jobs/7d2ed44f-6934-4326-8087-e58d95cdf600/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n40.json) |
| QESEM | TFIM n=40 | [665229b6-ebcf-4027-a0c0-07f4298be76a](ibm_enriched_jobs/jobs/665229b6-ebcf-4027-a0c0-07f4298be76a/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/665229b6-ebcf-4027-a0c0-07f4298be76a/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n40.json) |
| IBM TREX + twirling | TFIM n=60 | [d8serhktqbtc73curps0](ibm_enriched_jobs/jobs/d8serhktqbtc73curps0/metadata.json) | 2026-06-22T08:09:44.370709+00:00 | C10 | [JSON](ibm_enriched_jobs/jobs/d8serhktqbtc73curps0/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n60.json) |
| IBM raw | TFIM n=60 | [d8seq9sbp3hs73830o90](ibm_enriched_jobs/jobs/d8seq9sbp3hs73830o90/metadata.json) | 2026-06-22T08:07:48.034327+00:00 | C10 | [JSON](ibm_enriched_jobs/jobs/d8seq9sbp3hs73830o90/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n60.json) |
| Q-CTRL | TFIM n=60 | [e6890fb9-566d-4f4e-be9b-ea9a6a5f9e86](ibm_enriched_jobs/jobs/e6890fb9-566d-4f4e-be9b-ea9a6a5f9e86/metadata.json) | 2026-06-22T08:29:51.915635+00:00 | C10 | [JSON](ibm_enriched_jobs/jobs/e6890fb9-566d-4f4e-be9b-ea9a6a5f9e86/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n60.json) |
| QESEM | TFIM n=60 | [93ac77b4-4fe6-47bd-b257-b9444355e6b0](ibm_enriched_jobs/jobs/93ac77b4-4fe6-47bd-b257-b9444355e6b0/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/93ac77b4-4fe6-47bd-b257-b9444355e6b0/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n60.json) |
| IBM TREX + twirling | TFIM n=80 | [d8sg00tbh0os73eo4mp0](ibm_enriched_jobs/jobs/d8sg00tbh0os73eo4mp0/metadata.json) | 2026-06-22T09:27:33.302890+00:00 | C11 | [JSON](ibm_enriched_jobs/jobs/d8sg00tbh0os73eo4mp0/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n80.json) |
| IBM raw | TFIM n=80 | [d8sfutkbp3hs73832ceg](ibm_enriched_jobs/jobs/d8sfutkbp3hs73832ceg/metadata.json) | 2026-06-22T09:25:34.758862+00:00 | C11 | [JSON](ibm_enriched_jobs/jobs/d8sfutkbp3hs73832ceg/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n80.json) |
| Q-CTRL | TFIM n=80 | [683fec4d-6773-4952-9f9e-25ceec279e21](ibm_enriched_jobs/jobs/683fec4d-6773-4952-9f9e-25ceec279e21/metadata.json) | 2026-06-22T09:32:25.890399+00:00 | C12 | [JSON](ibm_enriched_jobs/jobs/683fec4d-6773-4952-9f9e-25ceec279e21/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n80.json) |
| QESEM | TFIM n=80 | [d82c6d70-e03b-40c7-b69f-cd6076d04cca](ibm_enriched_jobs/jobs/d82c6d70-e03b-40c7-b69f-cd6076d04cca/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/d82c6d70-e03b-40c7-b69f-cd6076d04cca/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n80.json) |
| IBM TREX + twirling | TFIM n=100 | [d8sl6jlposuc738nfum0](ibm_enriched_jobs/jobs/d8sl6jlposuc738nfum0/metadata.json) | 2026-06-22T15:23:02.003595+00:00 | C13 | [JSON](ibm_enriched_jobs/jobs/d8sl6jlposuc738nfum0/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n100.json) |
| IBM raw | TFIM n=100 | [d8skudtposuc738nfilg](ibm_enriched_jobs/jobs/d8skudtposuc738nfilg/metadata.json) | 2026-06-22T15:07:48.787846+00:00 | C13 | [JSON](ibm_enriched_jobs/jobs/d8skudtposuc738nfilg/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n100.json) |
| Q-CTRL | TFIM n=100 | [e78d8b74-4a29-40e7-ad19-d2a4993e6464](ibm_enriched_jobs/jobs/e78d8b74-4a29-40e7-ad19-d2a4993e6464/metadata.json) | 2026-06-22T15:56:55.165036+00:00 | C13 | [JSON](ibm_enriched_jobs/jobs/e78d8b74-4a29-40e7-ad19-d2a4993e6464/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n100.json) |
| QESEM | TFIM n=100 | [6e591dc1-f7ab-427b-a8d9-cc674d71e008](ibm_enriched_jobs/jobs/6e591dc1-f7ab-427b-a8d9-cc674d71e008/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/6e591dc1-f7ab-427b-a8d9-cc674d71e008/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n100.json) |
| IBM TREX + twirling | TFIM n=120 | [d8t25u5posuc738o2ehg](ibm_enriched_jobs/jobs/d8t25u5posuc738o2ehg/metadata.json) | 2026-06-23T07:27:46.214740+00:00 | C15 | [JSON](ibm_enriched_jobs/jobs/d8t25u5posuc738o2ehg/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n120.json) |
| IBM raw | TFIM n=120 | [d8t1ahlposuc738o14dg](ibm_enriched_jobs/jobs/d8t1ahlposuc738o14dg/metadata.json) | 2026-06-23T06:08:19.189754+00:00 | C14 | [JSON](ibm_enriched_jobs/jobs/d8t1ahlposuc738o14dg/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n120.json) |
| Q-CTRL | TFIM n=120 | [cbba293e-5e58-4f36-8f47-2c64e3fe0fe7](ibm_enriched_jobs/jobs/cbba293e-5e58-4f36-8f47-2c64e3fe0fe7/metadata.json) | 2026-06-23T07:48:57.094725+00:00 | C15 | [JSON](ibm_enriched_jobs/jobs/cbba293e-5e58-4f36-8f47-2c64e3fe0fe7/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n120.json) |
| QESEM | TFIM n=120 | [a4ce15be-ae59-44a9-b011-4d2780d87c33](ibm_enriched_jobs/jobs/a4ce15be-ae59-44a9-b011-4d2780d87c33/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/a4ce15be-ae59-44a9-b011-4d2780d87c33/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n120.json) |
| IBM TREX + twirling | TFIM n=130 | [d8tttalbh0os73eq6ejg](ibm_enriched_jobs/jobs/d8tttalbh0os73eq6ejg/metadata.json) | 2026-06-24T13:42:28.397067+00:00 | C16 | [JSON](ibm_enriched_jobs/jobs/d8tttalbh0os73eq6ejg/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n130.json) |
| IBM raw | TFIM n=130 | [d8tt4ddposuc738p9e4g](ibm_enriched_jobs/jobs/d8tt4ddposuc738p9e4g/metadata.json) | 2026-06-24T13:41:46.845006+00:00 | C16 | [JSON](ibm_enriched_jobs/jobs/d8tt4ddposuc738p9e4g/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n130.json) |
| Q-CTRL | TFIM n=130 | [fdc2aa2e-a8c8-4681-ac7f-d3d16560b6c2](ibm_enriched_jobs/jobs/fdc2aa2e-a8c8-4681-ac7f-d3d16560b6c2/metadata.json) | 2026-06-24T14:40:24.314918+00:00 | C16 | [JSON](ibm_enriched_jobs/jobs/fdc2aa2e-a8c8-4681-ac7f-d3d16560b6c2/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n130.json) |
| QESEM | TFIM n=130 | [a3f21783-ecae-4aa5-b856-9f40f4317e07](ibm_enriched_jobs/jobs/a3f21783-ecae-4aa5-b856-9f40f4317e07/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/a3f21783-ecae-4aa5-b856-9f40f4317e07/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n130.json) |
| IBM TREX + twirling | TFIM n=140 | [d8u0i0lposuc738pdsv0](ibm_enriched_jobs/jobs/d8u0i0lposuc738pdsv0/metadata.json) | 2026-06-24T18:26:39.582807+00:00 | C18 | [JSON](ibm_enriched_jobs/jobs/d8u0i0lposuc738pdsv0/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n140.json) |
| IBM raw | TFIM n=140 | [d8tuvn5posuc738pbs2g](ibm_enriched_jobs/jobs/d8tuvn5posuc738pbs2g/metadata.json) | 2026-06-24T15:47:25.311595+00:00 | C17 | [JSON](ibm_enriched_jobs/jobs/d8tuvn5posuc738pbs2g/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n140.json) |
| Q-CTRL | TFIM n=140 | [7cd1ceca-76ec-4a85-b07a-28d7be62b11f](ibm_enriched_jobs/jobs/7cd1ceca-76ec-4a85-b07a-28d7be62b11f/metadata.json) | 2026-06-24T20:06:34.632044+00:00 | C19 | [JSON](ibm_enriched_jobs/jobs/7cd1ceca-76ec-4a85-b07a-28d7be62b11f/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n140.json) |
| QESEM | TFIM n=140 | [aa25a037-ffbc-4b16-afd0-2d8598b6dc61](ibm_enriched_jobs/jobs/aa25a037-ffbc-4b16-afd0-2d8598b6dc61/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/aa25a037-ffbc-4b16-afd0-2d8598b6dc61/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n140.json) |
| IBM TREX + twirling | TFIM n=150 | [d8u56t4tqbtc73d196m0](ibm_enriched_jobs/jobs/d8u56t4tqbtc73d196m0/metadata.json) | 2026-06-24T22:00:21.661453+00:00 | C20 | [JSON](ibm_enriched_jobs/jobs/d8u56t4tqbtc73d196m0/experiments/tfim_probe-10K-8sites/IBM_TREX_TWIRLING_TFIM_n150.json) |
| IBM raw | TFIM n=150 | [d8u3t5stqbtc73d17b0g](ibm_enriched_jobs/jobs/d8u3t5stqbtc73d17b0g/metadata.json) | 2026-06-24T21:59:57.490384+00:00 | C20 | [JSON](ibm_enriched_jobs/jobs/d8u3t5stqbtc73d17b0g/experiments/tfim_probe-10K-8sites/IBM_RAW_TFIM_n150.json) |
| Q-CTRL | TFIM n=150 | [6bda7873-b35f-474c-a9e2-be3fef82c862](ibm_enriched_jobs/jobs/6bda7873-b35f-474c-a9e2-be3fef82c862/metadata.json) | 2026-06-24T22:44:12.994676+00:00 | C20 | [JSON](ibm_enriched_jobs/jobs/6bda7873-b35f-474c-a9e2-be3fef82c862/experiments/tfim_probe-10K-8sites/QCTRL_TFIM_n150.json) |
| QESEM | TFIM n=150 | [32fc35fb-af5d-4a0e-afb6-0fc118fcfc51](ibm_enriched_jobs/jobs/32fc35fb-af5d-4a0e-afb6-0fc118fcfc51/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/32fc35fb-af5d-4a0e-afb6-0fc118fcfc51/experiments/tfim_probe-10K-8sites/QESEM_TFIM_n150.json) |

### tfim_probe-16layers-full-chain

| Provider | Conditions | Job metadata | Execution start (UTC) | Snapshot | Original experiment copy |
| --- | --- | --- | --- | --- | --- |
| IBM TREX + twirling | TFIM n=25 | [d8vnrm6mvj5c73ei6jt0](ibm_enriched_jobs/jobs/d8vnrm6mvj5c73ei6jt0/metadata.json) | 2026-06-27T07:39:21.754553+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d8vnrm6mvj5c73ei6jt0/experiments/tfim_probe-16layers-full-chain/IBM_TREX_TWIRLING_TFIM_n25.json) |
| IBM raw | TFIM n=25 | [d8vmvpemvj5c73ei5140](ibm_enriched_jobs/jobs/d8vmvpemvj5c73ei5140/metadata.json) | 2026-06-27T06:41:56.484547+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d8vmvpemvj5c73ei5140/experiments/tfim_probe-16layers-full-chain/IBM_RAW_TFIM_n25.json) |
| Q-CTRL | TFIM n=25 | [3a92da7c-e583-4ab4-a207-7ef261f91961](ibm_enriched_jobs/jobs/3a92da7c-e583-4ab4-a207-7ef261f91961/metadata.json) | 2026-06-27T09:12:15.907842+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/3a92da7c-e583-4ab4-a207-7ef261f91961/experiments/tfim_probe-16layers-full-chain/QCTRL_TFIM_n25.json) |
| QESEM | TFIM n=25 | [e8b36bbc-426c-45db-913f-3e6b9c23b3c6](ibm_enriched_jobs/jobs/e8b36bbc-426c-45db-913f-3e6b9c23b3c6/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/e8b36bbc-426c-45db-913f-3e6b9c23b3c6/experiments/tfim_probe-16layers-full-chain/QESEM_TFIM_n25.json) |
| IBM TREX + twirling | TFIM n=50 | [d8vr5ggpknjs73a1h7og](ibm_enriched_jobs/jobs/d8vr5ggpknjs73a1h7og/metadata.json) | 2026-06-27T11:23:47.418391+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d8vr5ggpknjs73a1h7og/experiments/tfim_probe-16layers-full-chain/IBM_TREX_TWIRLING_TFIM_n50.json) |
| IBM raw | TFIM n=50 | [d8vq2qo6c68s73ah66f0](ibm_enriched_jobs/jobs/d8vq2qo6c68s73ah66f0/metadata.json) | 2026-06-27T10:27:41.545741+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d8vq2qo6c68s73ah66f0/experiments/tfim_probe-16layers-full-chain/IBM_RAW_TFIM_n50.json) |
| Q-CTRL | TFIM n=50 | [98a979a2-53bc-4c47-8dcb-3068c66a7d5f](ibm_enriched_jobs/jobs/98a979a2-53bc-4c47-8dcb-3068c66a7d5f/metadata.json) | 2026-06-27T12:57:59.407404+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/98a979a2-53bc-4c47-8dcb-3068c66a7d5f/experiments/tfim_probe-16layers-full-chain/QCTRL_TFIM_n50.json) |
| QESEM | TFIM n=50 | [8dcc5f45-524f-4973-90f7-aac50f701c64](ibm_enriched_jobs/jobs/8dcc5f45-524f-4973-90f7-aac50f701c64/metadata.json) | Unavailable | Unknown: No discoverable Runtime children | [JSON](ibm_enriched_jobs/jobs/8dcc5f45-524f-4973-90f7-aac50f701c64/experiments/tfim_probe-16layers-full-chain/QESEM_TFIM_n50.json) |
| IBM TREX + twirling | TFIM n=75 | [d8vtocopknjs73a1l2og](ibm_enriched_jobs/jobs/d8vtocopknjs73a1l2og/metadata.json) | 2026-06-27T14:23:12.853243+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d8vtocopknjs73a1l2og/experiments/tfim_probe-16layers-full-chain/IBM_TREX_TWIRLING_TFIM_n75.json) |
| IBM raw | TFIM n=75 | [d8vtd406c68s73ahb2fg](ibm_enriched_jobs/jobs/d8vtd406c68s73ahb2fg/metadata.json) | 2026-06-27T14:13:22.727274+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d8vtd406c68s73ahb2fg/experiments/tfim_probe-16layers-full-chain/IBM_RAW_TFIM_n75.json) |
| Q-CTRL | TFIM n=75 | [aa62ab44-d7d3-4e61-8408-c76593295f23](ibm_enriched_jobs/jobs/aa62ab44-d7d3-4e61-8408-c76593295f23/metadata.json) | 2026-06-27T15:12:05.814925+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/aa62ab44-d7d3-4e61-8408-c76593295f23/experiments/tfim_probe-16layers-full-chain/QCTRL_TFIM_n75.json) |
| IBM TREX + twirling | TFIM n=100 | [d900e8propqc738d4t90](ibm_enriched_jobs/jobs/d900e8propqc738d4t90/metadata.json) | 2026-06-27T17:23:48.854607+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d900e8propqc738d4t90/experiments/tfim_probe-16layers-full-chain/IBM_TREX_TWIRLING_TFIM_n100.json) |
| IBM raw | TFIM n=100 | [d8vvclopknjs73a1nf4g](ibm_enriched_jobs/jobs/d8vvclopknjs73a1nf4g/metadata.json) | 2026-06-27T16:27:37.972091+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d8vvclopknjs73a1nf4g/experiments/tfim_probe-16layers-full-chain/IBM_RAW_TFIM_n100.json) |
| Q-CTRL | TFIM n=100 | [29a732de-9d31-4304-86bc-7b5eb67578bf](ibm_enriched_jobs/jobs/29a732de-9d31-4304-86bc-7b5eb67578bf/metadata.json) | 2026-06-27T18:57:57.077905+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/29a732de-9d31-4304-86bc-7b5eb67578bf/experiments/tfim_probe-16layers-full-chain/QCTRL_TFIM_n100.json) |
| IBM TREX + twirling | TFIM n=125 | [d903vd1ropqc738da780](ibm_enriched_jobs/jobs/d903vd1ropqc738da780/metadata.json) | 2026-06-27T21:25:10.081423+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d903vd1ropqc738da780/experiments/tfim_probe-16layers-full-chain/IBM_TREX_TWIRLING_TFIM_n125.json) |
| IBM raw | TFIM n=125 | [d902n1emvj5c73eimnj0](ibm_enriched_jobs/jobs/d902n1emvj5c73eimnj0/metadata.json) | 2026-06-27T20:46:08.243660+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/d902n1emvj5c73eimnj0/experiments/tfim_probe-16layers-full-chain/IBM_RAW_TFIM_n125.json) |
| Q-CTRL | TFIM n=125 | [e3c41fb7-3dd8-4648-ba29-035cd66270ec](ibm_enriched_jobs/jobs/e3c41fb7-3dd8-4648-ba29-035cd66270ec/metadata.json) | 2026-06-27T23:17:45.939048+00:00 | C21 | [JSON](ibm_enriched_jobs/jobs/e3c41fb7-3dd8-4648-ba29-035cd66270ec/experiments/tfim_probe-16layers-full-chain/QCTRL_TFIM_n125.json) |

## Implication for the reviewer request

The existing datasets span multiple reported calibration snapshots, but this is not equivalent to repeating a fixed subset for each provider across multiple windows. Within each original folder, every saved algorithm/width/provider combination appears only once. Differences across provider snapshots can therefore be a timing confound rather than repeated evidence. No claim about equality of circuits/settings across different folders is made. The planned controlled repetitions remain a separate question.

