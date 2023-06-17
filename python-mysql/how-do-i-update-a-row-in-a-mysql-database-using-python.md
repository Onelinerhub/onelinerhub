# How do I update a row in a MySQL database using Python?
// plain

Updating a row in a MySQL database using Python is a relatively straightforward process. The following example code block will update a row in the 'customers' table of a database named 'mydatabase' with the customer's name changed from 'John Doe' to 'John Smith':

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET name = 'John Smith' WHERE name = 'John Doe'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
```

## Output example

```
1 record(s) affected
```

## Code explanation

- `import mysql.connector`: imports the necessary modules to connect to and query a MySQL database.
- `mydb = mysql.connector.connect(...)`: establishes a connection to the MySQL database.
- `mycursor = mydb.cursor()`: creates a cursor object used to execute SQL queries on the database.
- `sql = "UPDATE customers SET name = 'John Smith' WHERE name = 'John Doe'"`: creates a SQL query string to update the 'name' field in the 'customers' table from 'John Doe' to 'John Smith'.
- `mycursor.execute(sql)`: executes the SQL query on the database.
- `mydb.commit()`: commits the changes to the database.
- `print(mycursor.rowcount, "record(s) affected")`: prints the number of affected records in the database.

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL UPDATE Statement](https://www.w3schools.com/sql/sql_update.asp)

onelinerhub: [How do I update a row in a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-update-a-row-in-a-mysql-database-using-python)