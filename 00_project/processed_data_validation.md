# Processed-data validation

Pipeline: `python -m final_project_stackfuel.pipeline` from the repository environment.

Validated outputs: four WIdO rows; 435 population rows; nine obesity estimates; eight disease-cost rows; thirteen date keys; four substances; seven inventory records; machine-readable dictionary, controls and scenario framework.

Automated tests validate RAW integrity, schemas, keys, coverage, units, plausible confidence intervals, duplicate exclusion, control totals and the explicit `not_calculated` scenario status. No analytical result depends on Power BI-only logic.
