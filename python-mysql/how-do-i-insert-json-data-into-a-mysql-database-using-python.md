# How do I insert JSON data into a MySQL database using Python?
// plain

To insert JSON data into a MySQL database using Python, you need to use the `json` module to convert the JSON data into a Python dictionary, and then use the `MySQL Connector/Python` to insert the data into the MySQL database.

The following example code will demonstrate how to do this:
```
import mysql.connector
import json

# Load JSON data into Python dictionary
with open('data.json') as json_file:
    data = json.load(json_file)

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="mydatabase"
)

# Create cursor object
mycursor = mydb.cursor()

# Insert data into database
for record in data:
    sql = "INSERT INTO mytable (name, address) VALUES (%s, %s)"
    val = (record['name'], record['address'])
    mycursor.execute(sql, val)

# Commit changes to database
mydb.commit()

# Close connection to database
mydb.close()
```

The code above does the following:
- Imports the `mysql.connector` and `json` modules.
- Loads the JSON data into a Python dictionary.
- Connects to the MySQL database.
- Creates a cursor object.
- Inserts the data into the database.
- Commits the changes to the database.
- Closes the connection to the database.

## Helpful links
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [Python JSON Module](https://docs.python.org/3/library/json.html)

onelinerhub: [How do I insert JSON data into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-insert-json-data-into-a-mysql-database-using-python)