import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

cnx = mysql.connector.connect(user=config.get('database', 'db_user'),
                              password=config.get('database', 'db_password'),
                              database=config.get('database', 'db_dbname'),
                              host='127.0.0.1')


def get_food_groups():
    cursor = cnx.cursor()
    cursor.execute('Select FdGrp_Desc From FOOD_GROUP_DESCRIPTION')
    column_names = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()

    return column_names, rows


def get_all_foods():
    cursor = cnx.cursor()
    cursor.execute('Select Long_Desc, Shrt_Desc From FOOD_DESCRIPTION')
    column_names = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()

    return column_names, rows

def get_company_products(input):
    cursor = cnx.cursor()
    args = (input)
    cursor.callproc('GetCompanyProducts', args)
    column_names = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()

    return column_names, rows


def get_food_group_desc_like(input):
    cursor = cnx.cursor()
    args = (input)
    cursor.callproc('GetFoodGroupDescLike', args)
    column_names = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()

    return column_names, rows

def get_food_long_des(input):
    cursor = cnx.cursor()
    args = (input)
    cursor.callproc('GetFoodLongDesc', args)
    column_names = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()

    return column_names, rows

def get_food_group_like_desc(input):
    cursor = cnx.cursor()
    args = (input)
    cursor.callproc('GetFoodGroupLikeDesc', args)
    column_names = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()

    return column_names, rows

def lookup_similar_food(input):
    cursor = cnx.cursor()
    args = (input)
    cursor.callproc('LookupSimilarFood', args)
    column_names = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()

    return column_names, rows

def lookup_food_nutrients(input):
    cursor = cnx.cursor()
    args = (input)
    cursor.callproc('LookupFoodNutrients', args)
    column_names = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()

    return column_names, rows