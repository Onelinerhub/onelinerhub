# How do I execute a MySQL script using Python?
// plain

To execute a MySQL script using Python, you can use the `mysql.connector` library. This library provides an API for connecting to and executing queries on a MySQL database.

An example of how to execute a MySQL script using Python is shown below:
```python
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="password",
  database="database_name"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the script
mycursor.execute("source /path/to/script.sql")

# Fetch the results
result = mycursor.fetchall()

# Print the results
print(result)
```

The code above will execute the SQL script located at `/path/to/script.sql` and print the results.

The code above consists of the following parts:

1. `import mysql.connector`: imports the `mysql.connector` library.
2. `mydb = mysql.connector.connect(...)`: connects to the MySQL database.
3. `mycursor = mydb.cursor()`: creates a cursor object.
4. `mycursor.execute("source /path/to/script.sql")`: executes the SQL script.
5. `result = mycursor.fetchall()`: fetches the results.
6. `print(result)`: prints the results.

## Helpful links

- [mysql.connector — MySQL Connector/Python 8.0.18 documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL :: MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html)

onelinerhub: [How do I execute a MySQL script using Python?](https://onelinerhub.com/python-mysql/how-do-i-execute-a-mysql-script-using-python)