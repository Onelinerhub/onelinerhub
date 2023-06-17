# How do I connect Python with MySQL using XAMPP?
// plain

In order to connect Python with MySQL using XAMPP, you need to install MySQL Connector Python module. MySQL Connector Python is the official Oracle-supported driver to connect MySQL through Python.

First, install the MySQL Connector Python module:
```
pip install mysql-connector-python
```

Next, create a connection object to the MySQL server, using the connection credentials.
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
# output: <mysql.connector.connection_cext.CMySQLConnection object at 0x7f3a4c3b4550>
```

Finally, create a cursor object to execute SQL queries.
```
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
# output: ('information_schema',)
#         ('mysql',)
#         ('performance_schema',)
#         ('sakila',)
#         ('sys',)
#         ('world',)
```

The following are the parts of the code and their explanation:
1. `pip install mysql-connector-python` - This command installs the MySQL Connector Python module.
2. `import mysql.connector` - This command imports the MySQL Connector Python module.
3. `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")` - This command creates a connection object to the MySQL server, using the connection credentials.
4. `mycursor = mydb.cursor()` - This command creates a cursor object to execute SQL queries.
5. `mycursor.execute("SHOW DATABASES")` - This command executes the SQL query to show the databases.
6. `for x in mycursor: print(x)` - This command prints the output of the SQL query.

## Helpful links

- [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/)
- [Connect Python to MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)

onelinerhub: [How do I connect Python with MySQL using XAMPP?](https://onelinerhub.com/python-mysql/how-do-i-connect-python-with-mysql-using-xampp)