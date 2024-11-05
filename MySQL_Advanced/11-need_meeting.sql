-- Task: 11. No table for a meeting - creates a view `need_meeting` listing students with a `score` under 80 and either no `last_meeting` date or a `last_meeting` date over one month old
-- The view `need_meeting` returns names of students who meet the criteria
-- Script can be executed on any database
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
