CREATE OR REPLACE VIEW fact_population_state_age_sex_sql AS
SELECT p.reference_date,p.year,p.state_code,g.state_name,p.sex_code,s.sex_label,p.age_code_official,a.age_label_official,p.age_years,p.age_group,p.population_persons,p.unit,p.quality_flag,p.census_basis,p.series_break_before,p.source_id,p.input_class,p.denominator
FROM population_processed p
JOIN dim_geography_sql g USING(state_code)
JOIN dim_sex_sql s USING(sex_code)
JOIN dim_age_sql a USING(age_code_official)
WHERE NOT p.is_age_total AND NOT p.is_sex_total;
