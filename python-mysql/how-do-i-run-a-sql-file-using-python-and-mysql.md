# How do I run a SQL file using Python and MySQL?
// plain

To run a SQL file using Python and MySQL, you can use the `mysql.connector` module. This module provides an interface for connecting to a MySQL database server and running SQL statements. The following example code will connect to a MySQL server and execute a SQL file:

```
import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password"
)

# Create a cursor
mycursor = mydb.cursor()

# Execute a SQL file
f = open('my_sql_file.sql', 'r')
sql_file = f.read()
mycursor.execute(sql_file)

# Close the cursor
mycursor.close()
```

This code will connect to the MySQL server, create a cursor, execute the SQL statements in the file `my_sql_file.sql`, and then close the cursor.

The code consists of the following parts:

1. Import the `mysql.connector` module.
2. Connect to the MySQL server using the `mysql.connector.connect()` function.
3. Create a cursor using the `mydb.cursor()` method.
4. Read the SQL file using the `open()` function and store it in a variable.
5. Execute the SQL statements in the file using the `mycursor.execute()` method.
6. Close the cursor using the `mycursor.close()` method.

For more information, see the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I run a SQL file using Python and MySQL?](https://onelinerhub.com/python-mysql/how-do-i-run-a-sql-file-using-python-and-mysql)