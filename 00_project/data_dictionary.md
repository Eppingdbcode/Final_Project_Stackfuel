# Data dictionary

The complete machine-readable dictionary is generated at `04_outputs/tables/data_dictionary.csv`. It records table, column, type, description, unit, denominator, input class, source and limitations for every delivered table.

Power BI must use the fact-table `input_class`, `source_id`, denominator and scope columns in tooltips or methods text. Units must never be combined across rows without filtering the unit first.
