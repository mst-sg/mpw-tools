# Expected results

- `python verify.py`: package checksums PASS; reports-consistent.json metadata consistent; reports-stale.json DRC layout_sha256 and layout_revision mismatch. Exit 0 only when all exercise assertions pass.
- Inspector: A 100×60 um; B 120×60 um; 2 cells, one top MST_DEMO_TOP, DBU 0.001 um, 3 layer/datatype pairs. Stored definitions contain 3 BOUNDARY records and 2 SREF records; flattened instance counts differ.
- Browser report checker with B, MST_DEMO_TOP, B, TEACHING-NO-PDK-v1: stale metadata yields 2 findings; consistent metadata yields none. Enter OTHER top cell: both reports disagree.
- Correct response to stale evidence: get the responsible engineer to repeat the appropriate approved verification and bind its evidence to the frozen candidate. Do not edit metadata to manufacture a pass.

No result above is foundry signoff or proof of a working chip.
