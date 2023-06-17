# How can I retrieve data from a MySQL table using Python?
// plain

Retrieving data from a MySQL table using Python is easy and can be done in a few steps.

First, we need to install the MySQL Connector/Python library. This library provides an API for connecting to a MySQL database and executing SQL commands.

```
pip install mysql-connector-python
```

Once the library is installed, we can connect to the MySQL database and retrieve data from the table.

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword"
)

# Create a cursor
mycursor = mydb.cursor()

# Select records from the table
mycursor.execute("SELECT * FROM your_table")

# Fetch all the records
records = mycursor.fetchall()

# Print the records
print(records)
```

## Output example

```
[('John', 'Doe', 33), ('Jane', 'Doe', 32)]
```

The code above consists of the following parts:

1. `import mysql.connector`: imports the MySQL Connector/Python library.
2. `mydb = mysql.connector.connect`: connects to the MySQL database.
3. `mycursor = mydb.cursor()`: creates a cursor object.
4. `mycursor.execute("SELECT * FROM your_table")`: executes a SQL query to select all records from the table.
5. `records = mycursor.fetchall()`: fetches all the records from the result set.
6. `print(records)`: prints the records.

For more information, see the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I retrieve data from a MySQL table using Python?](https://onelinerhub.com/python-mysql/how-can-i-retrieve-data-from-a-mysql-table-using-python)