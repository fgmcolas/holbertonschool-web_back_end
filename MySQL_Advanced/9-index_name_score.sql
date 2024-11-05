-- Task: 9. Optimize search and score - creates an index `idx_name_first_score` on the table `names` for the first letter of the column `name` and the column `score`
-- Script can be executed on any database
CREATE INDEX idx_name_first_score ON names(name(1), score);