# How do I add a row to a MySQL database using Python?
// plain

To add a row to a MySQL database using Python, you can use the `cursor.execute()` method. This method takes a SQL query as an argument and executes it. The following example code will add a row to a table called 'users' in a MySQL database:

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create a SQL query
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
val = ("John", "john@example.com")

# Execute the query
mycursor.execute(sql, val)

# Commit the changes to the database
mydb.commit()

# Print the number of rows affected
print(mycursor.rowcount, "record inserted.")
```

## Output example

```
1 record inserted.
```

The code consists of the following parts:

1. `import mysql.connector` - imports the mysql connector library to allow Python to communicate with MySQL databases.
2. `mydb = mysql.connector.connect(...)` - establishes a connection to the MySQL database.
3. `mycursor = mydb.cursor()` - creates a cursor object which is used to execute queries.
4. `sql = "INSERT INTO users (name, email) VALUES (%s, %s)"` - creates a SQL query which will insert a row into the 'users' table.
5. `val = ("John", "john@example.com")` - defines the values to be inserted into the table.
6. `mycursor.execute(sql, val)` - executes the SQL query with the given values.
7. `mydb.commit()` - commits the changes to the database.
8. `print(mycursor.rowcount, "record inserted.")` - prints the number of rows affected.

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL INSERT INTO Statement](https://www.w3schools.com/sql/sql_insert.asp)

onelinerhub: [How do I add a row to a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-add-a-row-to-a-mysql-database-using-python)