# How do I use Python to connect to a MySQL database?
// plain

Connecting to a MySQL database with Python is a straightforward process. First, you must install the `mysql-connector-python` package using the `pip` command.

```
pip install mysql-connector-python
```

Once installed, you can use the `mysql.connector.connect()` method to connect to the database. You must provide the `host`, `user`, `password`, and `database` parameters.

```
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database"
)
```

Once connected, you can use the `cursor()` method to create a cursor object for executing SQL queries.

```
cursor = db.cursor()
```

You can then use the `execute()` method of the cursor object to execute SQL queries.

```
cursor.execute("SELECT * FROM table")

for row in cursor.fetchall():
    print(row)
```

## Output example

```
(1, 'John', 'Doe')
(2, 'Jane', 'Doe')
```

For more information, see the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I use Python to connect to a MySQL database?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-connect-to-a-mysql-database)