# GENESIS hero processing and lineage

The pipeline validates SHA-256, ZIP membership, shape, source code, unit and duplicates; normalizes official codes and types; derives documented age groups and census basis; and persists all 22,080 records as Parquet. Official totals remain in processed for controls but are excluded from the additive fact.

DuckDB reads Parquet, joins real dimensions, validates quality, aggregates by state/sex/age group and calculates shares and dense rankings with window functions. Pandas and SQL reconcile one-to-one. Machine-readable lineage records source columns, rules, units, denominators, evidence class and limitations.

Funnel: 22,080 RAW → 22,080 processed → 14,560 fact + 1,280 age/sex summaries + 80 state summaries → Power BI. No row is synthesized to increase volume.
