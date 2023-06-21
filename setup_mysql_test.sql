-- A database hbnb_test_db
-- A new user hbnb_test (in localhost)
-- The password of hbnb_test should be set to hbnb_test_pwd
-- hbnb_test should have all privileges on the database hbnb_test_db 
-- hbnb_test should have SELECT privilege on the database performance_schema 
-- If the database hbnb_test_db or the user hbnb_test already exists, 
-- your script should not fail

-- Script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creating new user,hbnb_test with * privileges on DB, hbnb_test_db
-- with password,hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Granting SELECT privilege for the user hbnb_test on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Granting * privileges to new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
