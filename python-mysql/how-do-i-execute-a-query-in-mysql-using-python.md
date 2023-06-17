# How do I execute a query in MySQL using Python?
// plain

To execute a query in MySQL using Python, you must first create a connection to the database. This can be done using the `mysql.connector` module. The following example code creates a connection to a MySQL database and executes a query to select all records from the `employees` table:

```
import mysql.connector

# Create connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="password",
  database="mydatabase"
)

# Execute query
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employees")

# Output query results
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

The code above will output the results of the query, for example:

```
(1, 'John', 'Doe', 'john@example.com')
(2, 'Mary', 'Moe', 'mary@example.com')
(3, 'Julie', 'Dooley', 'julie@example.com')
```

The code consists of the following parts:

1. `import mysql.connector`: imports the `mysql.connector` module, which contains the functions needed to connect to a MySQL database.

2. `mydb = mysql.connector.connect(...)`: creates a connection to the MySQL database. The connection is stored in the `mydb` variable.

3. `mycursor = mydb.cursor()`: creates a cursor object, which is used to execute the query.

4. `mycursor.execute("SELECT * FROM employees")`: executes the query to select all records from the `employees` table.

5. `myresult = mycursor.fetchall()`: fetches all the results of the query and stores them in the `myresult` variable.

6. `for x in myresult: print(x)`: iterates through the results of the query and prints them.

For more information on connecting to and executing queries in MySQL using Python, see the following links:

- [Connecting to MySQL Using Connector/Python](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
- [Executing Statements Using Connector/Python](https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-execute.html)

onelinerhub: [How do I execute a query in MySQL using Python?](https://onelinerhub.com/python-mysql/how-do-i-execute-a-query-in-mysql-using-python)