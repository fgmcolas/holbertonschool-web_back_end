-- Task: 4. Add user privileges - grants `INSERT` privileges to a user on a specific database
-- Script can be executed on any MySQL server with appropriate privileges
CREATE TRIGGER order_decrease BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
