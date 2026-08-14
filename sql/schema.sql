CREATE OR REPLACE TABLE population_processed AS
SELECT * FROM read_parquet('{{processed_path}}');
CREATE OR REPLACE TABLE dim_geography_sql AS SELECT DISTINCT state_code, state_name FROM population_processed;
CREATE OR REPLACE TABLE dim_sex_sql AS SELECT DISTINCT sex_code, sex_label, is_sex_total FROM population_processed;
CREATE OR REPLACE TABLE dim_age_sql AS SELECT DISTINCT age_code_official, age_label_official, age_years, age_group, is_age_total FROM population_processed;
