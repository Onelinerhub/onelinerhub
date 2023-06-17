# How do I connect to a MySQL Lite database using Python?
// plain

To connect to a MySQL Lite database using Python, the following steps are needed:

1. Install the MySQL driver for Python: `pip install mysql-connector-python`
2. Import the driver into your code: `import mysql.connector`
3. Create a connection object: `conn = mysql.connector.connect(host='localhost', database='dbname', user='username', password='password')`
4. Create a cursor object: `cursor = conn.cursor()`
5. Execute your SQL query: `cursor.execute('SELECT * FROM table_name')`
6. Fetch the results of the query: `rows = cursor.fetchall()`
7. Close the connection: `conn.close()`

## Example code

```
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='dbname', user='username', password='password')

cursor = conn.cursor()

cursor.execute('SELECT * FROM table_name')

rows = cursor.fetchall()

print(rows)

conn.close()
```

## Output example

```
[('value1', 'value2', 'value3'), ('value4', 'value5', 'value6')]
```

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html)
- [MySQL Connector/Python API Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How do I connect to a MySQL Lite database using Python?](https://onelinerhub.com/python-mysql/how-do-i-connect-to-a-mysql-lite-database-using-python)