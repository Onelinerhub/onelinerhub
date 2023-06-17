# How do I use Python and MySQL to execute multiple statements?
// plain

If you want to execute multiple statements in Python and MySQL, you can use the `cursor.execute()` method. This method takes a single parameter, which is a string containing one or more SQL statements.

For example, the following code block will execute two SQL statements:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s); SELECT * FROM customers"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

This code will output the following:

```
(1, 'John', 'Highway 21')
```

The code consists of the following parts:
1. Importing the `mysql.connector` module
2. Establishing a connection to the MySQL database
3. Creating a cursor object
4. Creating a string containing two SQL statements
5. Executing the SQL statements
6. Fetching the results
7. Iterating through the results and printing each row

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I use Python and MySQL to execute multiple statements?](https://onelinerhub.com/python-mysql/how-do-i-use-python-and-mysql-to-execute-multiple-statements)