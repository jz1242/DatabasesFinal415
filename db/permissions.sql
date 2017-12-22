%GRANT SELECT ON FOOD_DESCRIPTION TO ENROLLED_;

%GRANT SELECT ON NUTRIENT_DATA TO PUBLIC;

%maybe for non-registered users
CREATE ROLE BasicUser;
GRANT SELECT
ON FOOD_DESCRIPTION
TO BasicUser;


%for logged in users
CREATE ROLE RegisterUser;
GRANT SELECT
ON FOOD_DESCRIPTION
TO RegisterUser;

%for administrators and any other people who have to maintain the database
CREATE ROLE Administrator;
GRANT SELECT, UPDATE, INSERT, DELETE
ON DATABASE project1
TO Administrator;
