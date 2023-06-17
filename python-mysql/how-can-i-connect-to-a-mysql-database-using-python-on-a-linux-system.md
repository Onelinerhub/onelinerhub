# How can I connect to a MySQL database using Python on a Linux system?
// plain

To connect to a MySQL database using Python on a Linux system, first you need to install the MySQL Connector for Python. This can be done using the pip command:

```
pip install mysql-connector-python
```

Once installed, you can create a connection object with the following code:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
```

The `host` argument can be set to the IP address of the MySQL server. The `user` and `passwd` arguments should be set to the username and password used to log into the MySQL server.

After running the code, the connection object is printed. This can be used to execute SQL queries, create tables, etc.

Parts of the code:
- `import mysql.connector`: imports the mysql.connector module
- `mydb = mysql.connector.connect()`: creates a connection object
- `host="localhost"`: sets the host to the IP address of the MySQL server
- `user="yourusername"`: sets the username used to log into the MySQL server
- `passwd="yourpassword"`: sets the password used to log into the MySQL server
- `print(mydb)`: prints the connection object

## Helpful links
- [MySQL Connector for Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Tutorial](https://www.w3schools.com/sql/default.asp)

onelinerhub: [How can I connect to a MySQL database using Python on a Linux system?](https://onelinerhub.com/python-mysql/how-can-i-connect-to-a-mysql-database-using-python-on-a-linux-system)