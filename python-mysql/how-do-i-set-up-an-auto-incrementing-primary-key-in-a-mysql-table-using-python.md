# How do I set up an auto-incrementing primary key in a MySQL table using Python?
// plain

To set up an auto-incrementing primary key in a MySQL table using Python, you can use the MySQL Connector/Python library.

The following example code will create a table called `users` with an auto-incrementing primary key column called `id`:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"

mycursor.execute(sql)
```

The above code will create a table called `users` with an auto-incrementing primary key column called `id`.

The parts of the code are as follows:

- `import mysql.connector`: imports the MySQL Connector/Python library
- `mydb = mysql.connector.connect(host="localhost", user="user", passwd="password")`: connects to the MySQL database
- `mycursor = mydb.cursor()`: creates a cursor object to execute SQL statements
- `sql = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"`: creates a SQL statement to create a table with an auto-incrementing primary key
- `mycursor.execute(sql)`: executes the SQL statement

## Helpful links

- [MySQL Connector/Python - Creating Tables](https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html)

onelinerhub: [How do I set up an auto-incrementing primary key in a MySQL table using Python?](https://onelinerhub.com/python-mysql/how-do-i-set-up-an-auto-incrementing-primary-key-in-a-mysql-table-using-python)