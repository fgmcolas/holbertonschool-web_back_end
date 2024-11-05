-- Task: 7. Search and score - adds an index `idx_score` on the `score` column of the `students` table to optimize search performance
-- Script can be executed on any database
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (
        SELECT AVG(score)
        FROM corrections AS C
        WHERE C.user_id = user_id
    );
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END;
//
DELIMITER ;
