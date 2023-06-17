# How can I keep a MySQL connection alive in Python?
// plain

The following code block can be used to keep a MySQL connection alive in Python:

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd"
)

# Create a Cursor object to execute queries
my_cursor = mydb.cursor()

# Keep the connection alive by running a query every 5 minutes
while True:
    my_cursor.execute("SELECT 1")
    time.sleep(300)
```

The code above will keep the MySQL connection alive by running a query every 5 minutes. This is done by creating a `mysql.connector.connect` object, which is used to create a `Cursor` object. Then, a query is executed in an infinite loop, with a `time.sleep()` of 5 minutes (300 seconds) between each query.

The parts of this code are:

1. `import mysql.connector`: This imports the `mysql.connector` module, which is used to connect to the MySQL database.
2. `mydb = mysql.connector.connect()`: This creates a `mysql.connector.connect` object, which is used to connect to the MySQL database.
3. `my_cursor = mydb.cursor()`: This creates a `Cursor` object, which is used to execute queries on the database.
4. `my_cursor.execute("SELECT 1")`: This executes a query on the database.
5. `time.sleep(300)`: This pauses the code for 5 minutes (300 seconds).

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Cursor Objects](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

onelinerhub: [How can I keep a MySQL connection alive in Python?](https://onelinerhub.com/python-mysql/how-can-i-keep-a-mysql-connection-alive-in-python)