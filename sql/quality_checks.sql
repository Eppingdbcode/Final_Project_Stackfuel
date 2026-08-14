CREATE OR REPLACE VIEW quality_checks AS
WITH checks AS (
 SELECT 'processed_row_count' AS check_name, COUNT(*)::DOUBLE AS actual, 22080::DOUBLE AS expected FROM population_processed
 UNION ALL SELECT 'duplicate_key_count', COUNT(*)::DOUBLE, 0::DOUBLE FROM (SELECT reference_date,state_code,sex_code,age_code_official FROM population_processed GROUP BY ALL HAVING COUNT(*)>1)
 UNION ALL SELECT 'negative_population_count', COUNT(*)::DOUBLE, 0::DOUBLE FROM population_processed WHERE population_persons<0
 UNION ALL SELECT 'state_count', COUNT(DISTINCT state_code)::DOUBLE, 16::DOUBLE FROM population_processed
)
SELECT *, CASE WHEN actual=expected THEN 'pass' ELSE 'fail' END AS status FROM checks;
