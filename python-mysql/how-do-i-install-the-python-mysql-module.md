# How do I install the Python MySQL module?
// plain

The Python MySQL module can be installed using the [pip](https://pypi.org/project/pip/) package manager. To install the module, open a command line and type:
```
pip install mysql-connector-python
```
This will install the module and any dependencies.

Once the module is installed, you can use it in your Python programs. For example:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd"
)

print(mydb)
```

This code will connect to a MySQL database and print the connection information.

## Code explanation


- `import mysql.connector`: imports the MySQL Connector/Python module
- `mydb = mysql.connector.connect()`: creates a connection to the MySQL database
- `host="localhost"`: specifies the hostname of the database server
- `user="user"`: specifies the username for the connection
- `passwd="passwd"`: specifies the password for the connection
- `print(mydb)`: prints the connection information

Here are some relevant links for further reading:

- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)

onelinerhub: [How do I install the Python MySQL module?](https://onelinerhub.com/python-mysql/how-do-i-install-the-python-mysql-module)