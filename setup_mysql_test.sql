<<<<<<< HEAD
-- a script that prepares a MySQL server for the project.
=======
-- a script that prepares a MySQL server for the project
>>>>>>> 9fead4fb810359e3b0276f04670de1192276c9e0

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
