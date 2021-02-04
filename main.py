import mysql.connector
from mysql.connector import Error
from datetime import date
from user import User

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

def execute_readquery(connex, query):
    # execute a read query on the DB - to get evry row form the users table
    # we need a query
    # place to store results
    result = None
    # cursor to operate
    cursor = connex.cursor()

    cursor.execute(query)
    result = cursor.fetchall()
    return result

# CRUD - Read
connection = create_connection("axaam-db.cgzvo3rucizz.us-east-1.rds.amazonaws.com","ammaaraziz360","hymvim-minnib-5torKa","cis3368_db")
select_users = "SELECT * FROM users"
users = execute_readquery(connection, select_users)
print(users)

# not using the class instance
for user in users:
    dob = user[3]
    today = date.today()
    dayinterval = today - dob
    print(user[1], "is", dayinterval.days), "days old"

# using the class instance
for user in users:
    # create instance and pass in the elements from the result users
    u = User(user[0], user[1], user[2], user[3])
    print(u.dateofbirth)

# CRUD - Create
def execute_query(connex, query):
    cursor = connex.cursor()
    cursor.execute(query)
    connex.commit()
    print("query executed sucessfully")

create_invoice_table = """
CREATE TABLE IF NOT EXISTS invoices (
    id INT AUTO_INCREMENT,
    amount INT,
    description VARCHAR(255) NOT NULL,
    user_id INTEGER UNSIGNED NOT NULL,
    FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
    PRIMARY KEY (id)
)
"""

execute_query(connection, create_invoice_table)

# crud update 
# insert a new entry into users table
query = "INSERT INTO users (firstname, lastname, dateofbirth) VALUES ('jane', 'doe', '2002-02-02')"
#execute_query(connection, query)

# add invoice to the invoice tabel
invoice_for_user = 1
invoice_amount = 50
invoice_description = "harry potter books"

query = "INSERT INTO invoices (amount, description, user_id) VALUES (%s, '%s', %s)" % (invoice_amount, invoice_description, invoice_for_user)

#execute_query(connection, query)

#update a record
new_amount = 30
update_invoice_query = """
UPDATE
    invoices
SET
    amount = %s
WHERE
    id = 1
""" % (new_amount)
#execute_query(connection, update_invoice_query)


# CRUD - Delete
# delete invoice entry from the invoice table
invoice_id_to_delete = 1
delete_statement = "DELETE FROM invoices WHERE id = %s" % (invoice_id_to_delete)
#execute_query(connection, delete_statement)

#delete invoice table
delete_table_statement = "drop table invoices"
#execute_query(connection, delete_table_statement)