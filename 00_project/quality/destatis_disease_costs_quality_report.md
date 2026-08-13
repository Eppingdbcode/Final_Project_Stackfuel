# Destatis disease-cost quality report

- Source: GENESIS Flat CSV in an unchanged ZIP; UTF-8; semicolon delimiter.
- Selected scope: `E10-E14` and `E65-E68`, years 2020 and 2023, two metrics per diagnosis.
- Key: `year + diagnosis_code + metric_code`; eight unique rows; no missing selected values.
- Units: million EUR for national totals and EUR per resident.
- Limitation: all payers; not GKV, avoidable cost or cost per case. `E10-E14` does not isolate type 2 diabetes.
