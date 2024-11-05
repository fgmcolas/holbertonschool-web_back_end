-- Task: 10. Safe divide - creates a function `SafeDiv` that divides two numbers, returning the result or `0` if the divisor is `0`
-- The function `SafeDiv` takes two parameters, `a` and `b` of type `INT`, and returns `a / b` or `0` if `b` equals `0`
-- Script can be executed on any database
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END //
DELIMITER ;
