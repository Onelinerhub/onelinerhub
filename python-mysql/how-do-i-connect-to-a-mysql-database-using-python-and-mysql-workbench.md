# How do I connect to a MySQL database using Python and MySQL Workbench?
// plain

To connect to a MySQL database using Python and MySQL Workbench, you need to install the appropriate Python library such as `mysql.connector` and `PyMySQL`.

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
```

## Output example

```
<mysql.connector.connection.MySQLConnection object at 0x7f631f3f2f28>
```

1. `import mysql.connector`: This imports the MySQL Connector Python library.
2. `mydb = mysql.connector.connect(...)`: This creates a connection to the MySQL database, using the parameters provided.
3. `host`: This is the address of the MySQL server.
4. `user`: This is the username used to authenticate with the MySQL server.
5. `passwd`: This is the password used to authenticate with the MySQL server.
6. `print(mydb)`: This prints the connection object to the console.

## Helpful links
* [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
* [PyMySQL Documentation](https://pymysql.readthedocs.io/en/latest/)

onelinerhub: [How do I connect to a MySQL database using Python and MySQL Workbench?](https://onelinerhub.com/python-mysql/how-do-i-connect-to-a-mysql-database-using-python-and-mysql-workbench)