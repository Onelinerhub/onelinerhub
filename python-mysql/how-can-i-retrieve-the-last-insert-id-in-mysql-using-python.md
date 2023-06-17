# How can I retrieve the last insert ID in MySQL using Python?
// plain

The last insert ID in MySQL can be retrieved using Python by executing a query on the database. This can be done using the [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-lastrowid.html) library.

The following example code block shows how to use the `lastrowid` method to retrieve the last insert ID:

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="mydatabase"
)

cursor = db.cursor()

# Execute an INSERT query
cursor.execute("INSERT INTO table1 (column1, column2) VALUES (value1, value2)")

# Retrieve the last insert ID
last_insert_id = cursor.lastrowid

print(last_insert_id)

# Output: 12
```

The `lastrowid` method returns an integer which is the last insert ID of the query. This can then be used to reference the row which was just inserted.

onelinerhub: [How can I retrieve the last insert ID in MySQL using Python?](https://onelinerhub.com/python-mysql/how-can-i-retrieve-the-last-insert-id-in-mysql-using-python)