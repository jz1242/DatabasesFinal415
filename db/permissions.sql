#GRANT SELECT ON FOOD_DESCRIPTION TO ENROLLED_;

#GRANT SELECT ON NUTRIENT_DATA TO PUBLIC;

#maybe for non-registered users

#for logged in users
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT
ON FOOD_DESCRIPTION
TO RegisterUser;

#for administrators and any other people who have to maintain the database
CREATE User 'Administrator'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES
ON project1.*
TO 'Administrator'@'localhost';