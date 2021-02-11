import mysql.connector
import main
# # read from console and save in variable
# value = input("Please enter a string:\n")

# # print string
# print(f'You entered the value: {value}')

# # output string
# message = "you entered %s" % (value)
# print(message)

#dictionaries
mydict = {
    'firstname': 'Jane',
    'lastname': 'Doe',
    'birthyear': 2001
}

print(mydict)
print(type(mydict))

print(mydict['lastname'])
print(mydict['birthyear'])

fname = mydict['firstname']
print(fname)

lanme2 = mydict.get("lastname")
print(lanme2)

mydict = {
    'firstname': 'Jane',
    'lastname': 'Doe',
    'birthyear': 2001,
    'children': ["jack", "john", "james"]
}
print(mydict)

mydict["birthyear"] = 2000
print(mydict)

mydict.update({"birthyear": 1900})
print(mydict)

if "children" in mydict:
    print("this person has children")

mydict['father'] = "Jeff"
print(mydict)

del mydict["father"]
print(mydict)

mydict.clear()
print(mydict)

# lists
mylist = ["apple", "strawberry", 300, [1,2,3], True]
print(mylist)

if 300 in mylist:
    print("300 in the list")

mylist.insert(2, "skafas")
print(mylist)

#dictionary
con = mysql.connector.connect(host="axaam-db.cgzvo3rucizz.us-east-1.rds.amazonaws.com", user="ammaaraziz360", passwd="hymvim-minnib-5torKa", database="cis3368_db")
curosr = con.cursor(dictionary=True)
sql = "SELECT * FROM users"
curosr.execute(sql)
rows = curosr.fetchall()

#iterate over rows
for row in rows:
    print(row)
    print(row["firstname"], row["lastname"])
    # operate on result like any other dict
    if row["firstname"] == "Ammaar":
        row["firstname"] = "otto"
    print(row)
print(rows)


# conn = main.create_connection("axaam-db.cgzvo3rucizz.us-east-1.rds.amazonaws.com","ammaaraziz360","hymvim-minnib-5torKa","cis3368_db")
# sql_statment = "SELECT * FROM users"
# users = main.execute_readquery(conn, sql_statment)
# print(users)
