#Get all company products
DELIMITER //
DROP PROCEDURE IF EXISTS GetCompanyProducts//
CREATE PROCEDURE GetCompanyProducts
    (IN input TEXT)
        BEGIN
            SELECT Long_Desc
            FROM FOOD_DESCRIPTION
            WHERE  ManufacName LIKE CONCAT('%',input,'%');
        END //
DELIMITER ;


#Get all food description like a phrase
DELIMITER //
DROP PROCEDURE IF EXISTS GetFoodGroupDescLike//
CREATE PROCEDURE GetFoodGroupDescLike
    (IN input TEXT)
        BEGIN
            SELECT *
            FROM FOOD_GROUP_DESCRIPTION
            WHERE FdGrp_Desc LIKE CONCAT('%',input,'%');
        END //
DELIMITER ;

#Get Ingredient list in a product
/*DELIMITER //
DROP PROCEDURE IF EXISTS GetFoodGroupDesc//
CREATE PROCEDURE GetFoodGroupDesc
        BEGIN
            SELECT FdGrp_Desc
            FROM FOOD_GROUP_DESCRIPTION;
        END //
DELIMITER ;*/


# Get entry based off long desc
DELIMITER //
DROP PROCEDURE IF EXISTS GetFoodLongDesc//
CREATE PROCEDURE GetFoodLongDesc
    (IN input varchar(20))
        BEGIN
            SELECT *
            FROM FOOD_DESCRIPTION
            WHERE Long_Desc LIKE CONCAT('%',input,'%');
        END //
DELIMITER ;

/*
# List all of the food groups.
DELIMITER //
DROP PROCEDURE IF EXISTS ListFoodGroups//
CREATE PROCEDURE ListFoodGroups
        BEGIN
            SELECT DISTINCT FdGrp_Desc
            FROM FOOD_GROUP_DESCRIPTION;
        END //
DELIMITER ;*/

# Look up food groups by keyword.
DELIMITER //
DROP PROCEDURE IF EXISTS GetFoodGroupLikeDesc//
CREATE PROCEDURE GetFoodGroupLikeDesc
    (IN input TEXT)
        BEGIN
            SELECT DISTINCT FdGrp_Desc
            FROM FOOD_GROUP_DESCRIPTION
            WHERE FdGrp_Desc LIKE CONCAT('%',input,'%');
        END //
DELIMITER ;

# Look up related foods by keyword.
DELIMITER //
DROP PROCEDURE IF EXISTS GetSimilarFood//
CREATE PROCEDURE LookupSimilarFood
    (IN input TEXT)
        BEGIN
            SELECT DISTINCT Long_Desc
            FROM FOOD_DESCRIPTION INNER JOIN WEIGHTS
            WHERE Long_Desc LIKE CONCAT('%',input,'%');
        END //
DELIMITER ;

# Look up specific type of food and its nutrients.
DELIMITER //
DROP PROCEDURE IF EXISTS LookupFoodNutrients//
CREATE PROCEDURE LookupFoodNutrients
    (IN input TEXT)
        BEGIN
            SELECT DISTINCT NBD_No, Long_Desc,
              Nuts_Val, Std_Error,
              NutrDesc, Units
            FROM
                NUTRIENT_DEFINITION NATURAL JOIN NUTRIENT_DATA NATURAL JOIN FOOD_DESCRIPTION AS Nutrient
            WHERE Nutrient.NBD_No IN (
                SELECT FOOD_DESCRIPTION.NBD_No
                FROM FOOD_DESCRIPTION NATURAL JOIN FOOD_GROUP_DESCRIPTION
                WHERE Long_Desc LIKE CONCAT('%',input,'%'));
        END //
DELIMITER ;