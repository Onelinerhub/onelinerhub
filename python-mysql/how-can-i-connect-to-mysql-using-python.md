# How can I connect to MySQL using Python?
// plain

To connect to MySQL using Python, you need to use a library such as [mysql.connector](https://dev.mysql.com/doc/connector-python/en/).

The following example code can be used to connect to a MySQL database and execute a query:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

The output of the above code would be a list of all rows in the customers table.

The code consists of the following parts:

1. `import mysql.connector`: This imports the mysql.connector library, which is used to connect to MySQL.

2. `mydb = mysql.connector.connect(host="localhost", user="user", passwd="password")`: This creates a connection to the MySQL database. The host, user, and passwd parameters are used to specify the connection details.

3. `mycursor = mydb.cursor()`: This creates a cursor object, which is used to execute queries.

4. `mycursor.execute("SELECT * FROM customers")`: This executes the query to select all rows from the customers table.

5. `myresult = mycursor.fetchall()`: This fetches all the results from the query.

6. `for x in myresult: print(x)`: This prints out the results of the query.

For more information, see the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I connect to MySQL using Python?](https://onelinerhub.com/python-mysql/how-can-i-connect-to-mysql-using-python)