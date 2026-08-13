# Integration quality report

The model uses a small star-like structure. `dim_date[date_key]` has unique keys and one-to-many relationships to each observed fact. `dim_substance[atc_code]` relates one-to-many to WIdO. Facts are not joined directly.

Population, GKV prescriptions, survey respondents and all-payer disease costs are different universes. Relationships provide filtering only and do not assert individual linkage or common denominators. Multi-year RKI periods retain distinct keys such as `2019/2020`; no artificial annual allocation is performed.
