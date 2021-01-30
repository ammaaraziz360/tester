import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connector = None

    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = db_name
    )
    
    print("Connection to mySQL DB was succesful")

    return connection

# call function to open connection
# aws endpoint
# username
connection = create_connection("axaam-db.cgzvo3rucizz.us-east-1.rds.amazonaws.com","ammaaraziz360","hymvim-minnib-5torKa","cis3368_db")

# execute a read query on the DB - to get evry row form the users table
# we need a query
query = "SELECT * FROM users"
# place to store results
result = None
# cursor to operate
cursor = connection.cursor()

cursor.execute(query)
result = cursor.fetchall()

print(result)





