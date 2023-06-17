# How do I set up a remote connection to a MySQL database using Python?
// plain

To set up a remote connection to a MySQL database using Python, you need to:
1. Install the MySQL connector for Python: `pip install mysql-connector-python`
2. Create a connection object:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password"
)
```
3. Create a cursor object: `mycursor = mydb.cursor()`
4. Execute a query: `mycursor.execute("SELECT * FROM customers")`
5. Fetch the results: `myresult = mycursor.fetchall()`
6. Iterate over the result set:
```
for x in myresult:
  print(x)
```
7. Close the connection: `mydb.close()`

## Code explanation
**
1. `pip install mysql-connector-python` - Install the MySQL connector for Python.
2. `import mysql.connector` - Import the MySQL connector module.
3. `mydb = mysql.connector.connect(host="localhost", user="user", passwd="password")` - Create a connection object to the MySQL database.
4. `mycursor = mydb.cursor()` - Create a cursor object to execute queries.
5. `mycursor.execute("SELECT * FROM customers")` - Execute a query to select all data from the customers table.
6. `myresult = mycursor.fetchall()` - Fetch the results of the query.
7. `for x in myresult: print(x)` - Iterate over the result set and print each row.
8. `mydb.close()` - Close the connection to the database.

**## Helpful links**
- [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector Python Tutorial](https://www.w3schools.com/python/python_mysql_getstarted.asp)

onelinerhub: [How do I set up a remote connection to a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-set-up-a-remote-connection-to-a-mysql-database-using-python)