import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connector = None

    connection = mysql.connector.connect(
        host = host_name,
        user = user_name
        passwd = user_password,
        datbase = db_name
    )
    
    print("Connection to mySQL DB was succesful")

    return connector

# aws endpoint
# username
connection = create_connection("","","","")