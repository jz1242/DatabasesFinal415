# List all of the food groups.
SELECT DISTINCT FdGrp_Desc
FROM FOOD_GROUP_DESCRIPTION;

# Look up food groups by keyword.
SELECT DISTINCT FdGrp_Desc
FROM FOOD_GROUP_DESCRIPTION
WHERE FdGrp_Desc LIKE '%cheese%';

# Look up related foods by keyword.
SELECT DISTINCT Long_Desc
FROM FOOD_DESCRIPTION INNER JOIN WEIGHTS
WHERE Long_Desc LIKE '%cheese%';

# Look up specific type of food and its nutrients.
SELECT DISTINCT NBD_No, Long_Desc,
  Nuts_Val, Std_Error,
  NutrDesc, Units
FROM
    NUTRIENT_DEFINITION NATURAL JOIN NUTRIENT_DATA NATURAL JOIN FOOD_DESCRIPTION AS Nutrient
WHERE Nutrient.NBD_No IN (
    SELECT FOOD_DESCRIPTION.NBD_No
    FROM FOOD_DESCRIPTION NATURAL JOIN FOOD_GROUP_DESCRIPTION
    WHERE Long_Desc LIKE '%cheese%');

