# How can I use object-oriented programming with Python and MySQL?
// plain

Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to represent data and methods. In Python, OOP is used to create objects that represent data and methods, and MySQL is used to store and retrieve data.

Here is an example of how to use OOP with Python and MySQL:

```python
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="passwd",
    database="database"
)

# Create a cursor
mycursor = mydb.cursor()

# Create a class to represent a table row
class table_row:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create a table row
row = table_row("John", 25)

# Insert the row into the table
sql = "INSERT INTO table (name, age) VALUES (%s, %s)"
val = (row.name, row.age)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

## Output example

```
1 record inserted.
```

The code above does the following:

1. Imports the `mysql.connector` module, which is used to connect to MySQL.
2. Connects to the MySQL database.
3. Creates a cursor, which is used to execute SQL statements.
4. Creates a class to represent a table row.
5. Creates an instance of the `table_row` class.
6. Inserts the row into the table using a SQL statement.
7. Commits the changes to the database.
8. Prints the number of rows inserted.

## Helpful links

- [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql_getstarted.asp)
- [Object-Oriented Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/)

onelinerhub: [How can I use object-oriented programming with Python and MySQL?](https://onelinerhub.com/python-mysql/how-can-i-use-object-oriented-programming-with-python-and-mysql)