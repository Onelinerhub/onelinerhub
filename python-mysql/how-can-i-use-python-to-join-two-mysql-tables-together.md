# How can I use Python to join two MySQL tables together?
// plain

Using Python to join two MySQL tables together requires the use of the `JOIN` clause in an `SELECT` statement. An example of this is shown below:
```python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="database"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

This code will output the results of joining the two tables together:
```
(1, 'John', 'Doe', 25, 'John', 'Doe', 25)
(2, 'Mary', 'Moe', 30, 'Mary', 'Moe', 30)
(3, 'Julie', 'Dooley', 40, 'Julie', 'Dooley', 40)
```

The code consists of the following parts:

1. `import mysql.connector`: This imports the MySQL Connector Python library that allows us to connect to a MySQL database.
2. `mydb = mysql.connector.connect(...)`: This establishes a connection to the MySQL database.
3. `mycursor = mydb.cursor()`: This creates a cursor object that allows us to execute SQL statements.
4. `sql = "SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id"`: This is the SQL statement that defines the `JOIN` clause to join the two tables together.
5. `mycursor.execute(sql)`: This executes the SQL statement.
6. `myresult = mycursor.fetchall()`: This fetches all the results of the SQL statement.
7. `for x in myresult: print(x)`: This prints out the results of the SQL statement.

For more information about joining MySQL tables with Python, please see the following links:

- [MySQL Connector Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL JOIN Clause](https://www.w3schools.com/sql/sql_join.asp)

onelinerhub: [How can I use Python to join two MySQL tables together?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-join-two-mysql-tables-together)