# How do I select a table from a MySQL database using Python?
// plain

To select a table from a MySQL database using Python, the following code can be used:
```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="database_name"
)

# Create a cursor (an object to interact with the database)
mycursor = mydb.cursor()

# Select a table
mycursor.execute("SELECT * FROM table_name")

# Fetch all the data from the table
myresult = mycursor.fetchall()

# Print the data
for row in myresult:
  print(row)
```

The code above will output the data from the selected table in the database.

## Code explanation

1. `import mysql.connector` - imports the MySQL Connector module, which is used to connect to a MySQL database.
2. `mydb = mysql.connector.connect(host="localhost", user="user", passwd="password", database="database_name")` - connects to the database.
3. `mycursor = mydb.cursor()` - creates a cursor object to interact with the database.
4. `mycursor.execute("SELECT * FROM table_name")` - selects a table from the database.
5. `myresult = mycursor.fetchall()` - fetches all the data from the selected table.
6. `for row in myresult: print(row)` - prints the data from the table.

#### ## Helpful links
- [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL SELECT Query](https://www.w3schools.com/sql/sql_select.asp)

onelinerhub: [How do I select a table from a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-select-a-table-from-a-mysql-database-using-python)