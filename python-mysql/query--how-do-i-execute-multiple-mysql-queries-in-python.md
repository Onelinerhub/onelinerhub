# query

How do I execute multiple MySQL queries in Python?
// plain

Python enables us to execute multiple MySQL queries using the `mysql.connector` module. To do this, we first need to establish a connection to the MySQL server using the `connect()` method. Then, we can use the `cursor()` method to create a cursor object which can execute multiple queries.

The following example demonstrates how to execute multiple MySQL queries in Python:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

sql1 = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val1 = ("John", "Highway 21")

sql2 = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val2 = ("Peter", "Lowstreet 4")

mycursor.execute(sql1, val1)
mycursor.execute(sql2, val2)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

## Output example

```
2 record inserted.
```

The code above consists of the following parts:
1. Importing the `mysql.connector` module.
2. Establishing a connection to the MySQL server using the `connect()` method.
3. Creating a cursor object using the `cursor()` method.
4. Defining the SQL queries and values to be inserted.
5. Executing the queries using the `execute()` method.
6. Committing the changes to the database.
7. Printing out the number of rows affected.

## Helpful links
* [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
* [MySQL Tutorial](https://www.w3schools.com/sql/default.asp)

onelinerhub: [query

How do I execute multiple MySQL queries in Python?](https://onelinerhub.com/python-mysql/query--how-do-i-execute-multiple-mysql-queries-in-python)