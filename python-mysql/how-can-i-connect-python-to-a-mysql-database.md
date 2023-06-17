# How can I connect Python to a MySQL database?
// plain

To connect Python to a MySQL database, you can use the `mysql.connector` module. This module is part of the [MySQL Connector/Python](https://dev.mysql.com/downloads/connector/python/) package.

In order to connect to a MySQL database, you will need to have the following information:
- Host name (e.g. `localhost` or `127.0.0.1`)
- User name
- Password
- Database name

The following example code connects to a MySQL database and prints out the version of the MySQL server:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

print(mydb.get_server_info())
```

## Output example

```
8.0.19
```

For more information, see the [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I connect Python to a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-connect-python-to-a-mysql-database)