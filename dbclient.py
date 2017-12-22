import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

cnx = mysql.connector.connect(user=config.get('database', 'db_user'),
                              password=config.get('database', 'db_password'),
                              host='127.0.0.1',
                              database=config.get('database', 'db_dbname'))

def 
