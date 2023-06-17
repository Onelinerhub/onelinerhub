# How can I connect to a MySQL database using Python?
// plain

To connect to a MySQL database using Python, you can use the [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/). This is an API developed by Oracle that allows you to connect to a MySQL database from Python. The following example code will connect to a MySQL database and print the version of the MySQL server:

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

# Print the MySQL server version
print(mydb.server_version)
```

This example code will output the version of the MySQL server, for example:

```
8.0.19
```

The code consists of the following parts:

1. `import mysql.connector`: imports the MySQL Connector/Python module.
2. `mydb = mysql.connector.connect`: connects to the MySQL server.
3. `print(mydb.server_version)`: prints the version of the MySQL server.

For more information on connecting to MySQL using Python, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I connect to a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-connect-to-a-mysql-database-using-python)