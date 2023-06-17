# How do I use MySQL bind variables in Python?
// plain

MySQL bind variables in Python are used to pass data from a Python application to a MySQL database. The data is passed in the form of a tuple, and the bind variables are used to refer to the data in the tuple.

For example, the following code block creates a connection to a MySQL database, creates a cursor, and then uses the cursor to execute a query with a bind variable:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

This will output: `1 record inserted.`

The code is composed of the following parts:

1. `import mysql.connector` imports the MySQL Connector/Python module.
2. `mydb = mysql.connector.connect(...)` creates a connection to the MySQL database.
3. `mycursor = mydb.cursor()` creates a cursor object.
4. `sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"` creates a string containing a SQL query with two bind variables.
5. `val = ("John", "Highway 21")` creates a tuple containing the data to be inserted.
6. `mycursor.execute(sql, val)` executes the query with the bind variables.
7. `mydb.commit()` commits the changes to the database.
8. `print(mycursor.rowcount, "record inserted.")` prints the number of records inserted.

For more information, see the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I use MySQL bind variables in Python?](https://onelinerhub.com/python-mysql/how-do-i-use-mysql-bind-variables-in-python)