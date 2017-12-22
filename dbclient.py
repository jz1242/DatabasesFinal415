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
