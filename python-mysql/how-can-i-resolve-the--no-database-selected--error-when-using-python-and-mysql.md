# How can I resolve the "no database selected" error when using Python and MySQL?
// plain

The "no database selected" error is an error that is raised when a user tries to execute a query in a MySQL database without first selecting a database. This error can be resolved by selecting a database before executing the query.

## Example code

```
# Connect to the MySQL server
conn = mysql.connector.connect(
    host="hostname",
    user="username",
    passwd="password"
)

# Select the database
cursor = conn.cursor()
cursor.execute("USE my_database")

# Execute the query
cursor.execute("SELECT * FROM my_table")
```

The code above first connects to the MySQL server using the `mysql.connector.connect()` method. It then selects the database with the `USE` command, and finally executes the query.

## Code explanation

* `mysql.connector.connect()` - This is a method used to connect to the MySQL server.
* `cursor.execute("USE my_database")` - This is the command used to select the database.
* `cursor.execute("SELECT * FROM my_table")` - This is the command used to execute the query.

## Helpful links
* [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
* [MySQL Database Tutorial](https://www.w3schools.com/sql/default.asp)

onelinerhub: [How can I resolve the "no database selected" error when using Python and MySQL?](https://onelinerhub.com/python-mysql/how-can-i-resolve-the--no-database-selected--error-when-using-python-and-mysql)