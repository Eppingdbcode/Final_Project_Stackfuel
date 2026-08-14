# GENESIS hero SQL layer

Executed by `hero_pipeline.py`: load persisted Parquet into DuckDB, validate
keys and counts, perform justified dimension joins, aggregate by state, sex
and age group, and rank states within each reference date. The reproducible
DuckDB database is ignored; analytical CSVs and controls are versioned.
