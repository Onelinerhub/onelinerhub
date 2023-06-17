# How do I install MySQL on Python?
// plain

To install MySQL on Python, you can use the `pip` package manager. To do this, open the command line and type:

```
pip install mysql-connector-python
```

This will install the `mysql-connector-python` package which allows you to connect to a MySQL database from Python.

Once the package is installed, you can use the following code to connect to a MySQL database:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
```

This will output something like this:

```
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f859d9e7f50>
```

The code above does the following:
- `import mysql.connector` - imports the `mysql.connector` module which provides the functions to connect to a MySQL database
- `mydb = mysql.connector.connect` - creates a connection object to connect to the MySQL database
- `host="localhost"` - specifies the hostname of the MySQL server
- `user="yourusername"` - specifies the username of the MySQL server
- `passwd="yourpassword"` - specifies the password of the MySQL server
- `print(mydb)` - prints the connection object

For more information on how to install MySQL on Python, please refer to the [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I install MySQL on Python?](https://onelinerhub.com/python-mysql/how-do-i-install-mysql-on-python)