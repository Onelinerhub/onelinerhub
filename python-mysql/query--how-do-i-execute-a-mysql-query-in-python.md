# query

How do I execute a MySQL query in Python?
// plain

To execute a MySQL query in Python, you need to install a MySQL connector such as [MySQL Connector/Python](https://dev.mysql.com/downloads/connector/python/). After the connector is installed, you can use the following code to connect to the MySQL server and execute a query:

```python
import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="mydatabase"
)

# Create a cursor to use for executing queries
cursor = conn.cursor()

# Execute the query
cursor.execute("SELECT * FROM mytable")

# Print the results
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
```

The code consists of the following parts:
1. Importing the MySQL connector: `import mysql.connector`
2. Connecting to the MySQL server: `conn = mysql.connector.connect(host="localhost", user="user", passwd="password", database="mydatabase")`
3. Creating a cursor to use for executing queries: `cursor = conn.cursor()`
4. Executing the query: `cursor.execute("SELECT * FROM mytable")`
5. Printing the results: `for row in cursor.fetchall(): print(row)`
6. Closing the connection: `conn.close()`

The output of the example code will be the results of the query, for example:
```
(1, 'John', 'Doe')
(2, 'Jane', 'Doe')
(3, 'Alice', 'Smith')
```

onelinerhub: [query

How do I execute a MySQL query in Python?](https://onelinerhub.com/python-mysql/query--how-do-i-execute-a-mysql-query-in-python)