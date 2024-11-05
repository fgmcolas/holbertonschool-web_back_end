-- Task: 0. We are all unique! - creates a table `users` with a unique constraint on the `id` column to ensure no duplicate entries
-- Script can be executed on any database
CREATE TABLE IF NOT EXISTS 'users' (
    'id' INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    'email' VARCHAR(255) NOT NULL UNIQUE,
    'name' VARCHAR(255)
);
