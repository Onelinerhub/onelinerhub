# How can I connect Python to a MySQL database using an ODBC driver?
// plain

To connect Python to a MySQL database using an ODBC driver, you need to install the relevant ODBC driver for the database you are using. For example, if you are using MySQL, you can install the MySQL ODBC driver. Once you have installed the driver, you can use the `pyodbc` library to connect to the database.

## Example code

```
import pyodbc

# Connect to the database
connection = pyodbc.connect("DRIVER={MySQL ODBC Driver};SERVER=localhost;DATABASE=my_database;UID=user;PWD=password")

# Execute a query
cursor = connection.cursor()
cursor.execute("SELECT * FROM my_table")

# Fetch the results
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)
```

## Output example

```
('John', 'Doe', 'john.doe@example.com')
('Jane', 'Doe', 'jane.doe@example.com')
```

## Code explanation


- `import pyodbc` - imports the `pyodbc` library which is used to connect to the database.
- `connection = pyodbc.connect("DRIVER={MySQL ODBC Driver};SERVER=localhost;DATABASE=my_database;UID=user;PWD=password")` - connects to the database using the ODBC driver. The string contains the necessary connection parameters such as the driver, server, database, user and password.
- `cursor = connection.cursor()` - creates a cursor object which is used to execute queries on the database.
- `cursor.execute("SELECT * FROM my_table")` - executes a query on the database.
- `rows = cursor.fetchall()` - fetches the results of the query.
- `for row in rows: print(row)` - prints the results of the query.

## Helpful links

- [Connecting to MySQL with Python](https://www.mysqltutorial.org/python-connecting-mysql-databases/)
- [pyodbc Documentation](https://github.com/mkleehammer/pyodbc/wiki)

onelinerhub: [How can I connect Python to a MySQL database using an ODBC driver?](https://onelinerhub.com/python-mysql/how-can-i-connect-python-to-a-mysql-database-using-an-odbc-driver)