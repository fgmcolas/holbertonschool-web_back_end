-- Task: 6. Best friends forever - creates a new `friends` table with columns `user_id` and `friend_id` to define relationships between users
-- Script can be executed on any database
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
//
DELIMITER ;
