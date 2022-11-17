-- A script that prepares a test MySQL server for the Chicken Creed project

-- Create the database cc_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS cc_test_db;

-- Create the user cc_test
CREATE USER IF NOT EXISTS'cc_test'@'localhost' IDENTIFIED BY 'cc_test_pwd';

-- Set privileges for user cc_test
USE cc_test_db;
GRANT ALL PRIVILEGES ON cc_test_db.* TO 'cc_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'cc_test'@'localhost';
