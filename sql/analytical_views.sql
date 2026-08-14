CREATE OR REPLACE VIEW population_age_sex_summary_sql AS
WITH grouped AS (
 SELECT reference_date,year,state_code,sex_code,age_group,census_basis,SUM(population_persons)::HUGEINT AS population_persons
 FROM fact_population_state_age_sex_sql GROUP BY reference_date,year,state_code,sex_code,age_group,census_basis
) SELECT * FROM grouped;
CREATE OR REPLACE VIEW population_state_summary_sql AS
WITH state_totals AS (
 SELECT reference_date,year,state_code,population_persons,census_basis FROM population_processed WHERE is_age_total AND is_sex_total
), ranked AS (
 SELECT *,100.0*population_persons/SUM(population_persons) OVER(PARTITION BY reference_date) AS national_share_pct,
 DENSE_RANK() OVER(PARTITION BY reference_date ORDER BY population_persons DESC) AS population_rank FROM state_totals
) SELECT * FROM ranked;
