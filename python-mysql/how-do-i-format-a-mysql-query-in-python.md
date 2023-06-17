# How do I format a MySQL query in Python?
// plain

The Python Database API Specification v2.0 provides a common interface for various database systems. To access MySQL databases from Python, you need to install the MySQL Connector/Python package.

To format a MySQL query in Python, you need to use the following syntax:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

The output of the above code will be:
```
('John', 'Highway 21', 'Yellow Garden 2')
```

The code consists of the following parts:
1. `import mysql.connector`: imports the MySQL Connector/Python package.
2. `mydb = mysql.connector.connect()`: creates a connection to the MySQL database.
3. `mycursor = mydb.cursor()`: creates a cursor to execute the query.
4. `sql = "SELECT * FROM customers WHERE address = %s"`: defines the SQL query.
5. `adr = ("Yellow Garden 2", )`: defines the parameters for the query.
6. `mycursor.execute(sql, adr)`: executes the query with the parameters.
7. `myresult = mycursor.fetchall()`: fetches the results of the query.
8. `for x in myresult:`: loops through the results.
9. `print(x)`: prints each result.

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I format a MySQL query in Python?](https://onelinerhub.com/python-mysql/how-do-i-format-a-mysql-query-in-python)