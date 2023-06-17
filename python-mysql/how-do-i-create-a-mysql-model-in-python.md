# How do I create a MySQL model in Python?
// plain

Creating a MySQL model in Python is relatively straightforward. To do this, you need to import the mysql.connector library, create a connection object, and then use the cursor object to execute queries.

```
import mysql.connector

# Create a connection object
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="passwd"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("CREATE DATABASE mydatabase")
```

The code above will create a database called "mydatabase".

To create a table in the database, you can use the following code:

```
# Create a table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Show tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

# Output:
# ('customers',)
```

The code above will create a table called "customers" and then show the tables in the database.

To insert data into the table, you can use the following code:

```
# Insert data
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# Output:
# 1 record inserted.
```

The code above will insert a record into the "customers" table.

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Tutorial](https://www.w3schools.com/sql/default.asp)

onelinerhub: [How do I create a MySQL model in Python?](https://onelinerhub.com/python-mysql/how-do-i-create-a-mysql-model-in-python)