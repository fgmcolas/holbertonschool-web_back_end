-- Task: 5. Who am I? - displays the current MySQL user
-- Script can be executed on any MySQL server
DELIMITER //
CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
