# How can I grant privileges to a user in a MySQL database using Python?
// plain

To grant privileges to a user in a MySQL database using Python, you can use the [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) library.

The following example code grants the `SELECT` privilege to the `user_name` user on the `test_db` database:
```
import mysql.connector

# Create connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

# Create cursor
cursor = db.cursor()

# Grant privilege
cursor.execute("GRANT SELECT ON test_db.* TO user_name")
```

The code consists of the following parts:
1. Import the `mysql.connector` library
2. Create a connection to the MySQL server
3. Create a cursor object
4. Execute the `GRANT` statement to grant the desired privilege

For more information, please refer to the [MySQL GRANT documentation](https://dev.mysql.com/doc/refman/8.0/en/grant.html).

onelinerhub: [How can I grant privileges to a user in a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-grant-privileges-to-a-user-in-a-mysql-database-using-python)