# How do I use Python to perform an INSERT ON DUPLICATE KEY UPDATE query in MySQL?
// plain

The `INSERT ON DUPLICATE KEY UPDATE` query in MySQL can be used to update or insert new data into a table. To do this in Python, the `MySQL Connector/Python` library can be used.

First, the `MySQL Connector/Python` library needs to be imported and a connection to the MySQL database needs to be established.

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)
```

Then, a cursor needs to be created to execute the query.

```python
mycursor = mydb.cursor()
```

Finally, the `INSERT ON DUPLICATE KEY UPDATE` query can be written and executed.

```python
sql = "INSERT INTO customers (name, address) VALUES (%s, %s) ON DUPLICATE KEY UPDATE address = %s"
val = ("John", "Highway 21", "Valley 345")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted/updated.")
```

## Output example

```
1 record inserted/updated.
```

The code above consists of the following parts:
1. `import mysql.connector` - imports the `MySQL Connector/Python` library.
2. `mydb = mysql.connector.connect(...)` - establishes a connection to the MySQL database.
3. `mycursor = mydb.cursor()` - creates a cursor to execute the query.
4. `sql = "INSERT INTO customers (name, address) VALUES (%s, %s) ON DUPLICATE KEY UPDATE address = %s"` - defines the `INSERT ON DUPLICATE KEY UPDATE` query.
5. `val = ("John", "Highway 21", "Valley 345")` - defines the values to be inserted/updated.
6. `mycursor.execute(sql, val)` - executes the query.
7. `mydb.commit()` - commits the changes to the database.

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL INSERT ON DUPLICATE KEY UPDATE Syntax](https://dev.mysql.com/doc/refman/8.0/en/insert-on-duplicate.html)

onelinerhub: [How do I use Python to perform an INSERT ON DUPLICATE KEY UPDATE query in MySQL?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-perform-an-insert-on-duplicate-key-update-query-in-mysql)