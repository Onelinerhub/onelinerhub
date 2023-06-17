# How do I count the number of rows in a MySQL database using Python?
// plain

To count the number of rows in a MySQL database using Python, you can use the cursor.execute() method. This method will execute an SQL query and return the result.

For example:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM your_table")

print(mycursor.rowcount, "rows")
```

The output of the above code will be the number of rows in your table, e.g. `100 rows`.

The code consists of the following parts:

1. Importing the `mysql.connector` library to access the MySQL database.
2. Connecting to the MySQL database using the `mysql.connector.connect()` method.
3. Creating a cursor object to execute an SQL query using the `mydb.cursor()` method.
4. Executing the SQL query using the `mycursor.execute()` method.
5. Printing the number of rows in the table using the `mycursor.rowcount` attribute.

For more information, please refer to the following links:

- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Cursor Objects](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

onelinerhub: [How do I count the number of rows in a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-count-the-number-of-rows-in-a-mysql-database-using-python)