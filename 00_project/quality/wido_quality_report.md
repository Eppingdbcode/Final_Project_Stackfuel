# WIdO quality report

- Encoding: Windows-1252; delimiter: semicolon; format: CSV.
- Analytical source: 2024 A10BJ group export, four unique ATC rows.
- Keys: `year + atc_code`; no missing analytical metrics and no duplicate keys.
- Units: thousand prescriptions, thousand DDD, thousand EUR, EUR/prescription and EUR/DDD.
- Reconciliation: prescriptions sum to 2,674.0 thousand and net costs to EUR 582,169.1 thousand.
- Duplicate control: the two Semaglutide-only RAW paths are byte-identical and excluded from analytical row construction.
- Limitation: 2024 cross-section only; no indication, private/self-pay, inpatient use or longitudinal inference.
