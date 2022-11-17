-- A script that prepares a MySQL server for the Chicken Creed project

-- Create the database cc_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS cc_dev_db;

-- Create the user cc_dev
CREATE USER IF NOT EXISTS'cc_dev'@'localhost' IDENTIFIED BY 'cc_dev_pwd';

-- Set privileges for user cc_dev
USE cc_dev_db;
GRANT ALL PRIVILEGES ON cc_dev_db.* TO 'cc_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'cc_dev'@'localhost';
