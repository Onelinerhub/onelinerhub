# How can I connect to a MySQL database using Python?
// plain

1. First, import the MySQL Connector Python module:
```import mysql.connector```

2. Next, create a connection to the database by calling the `connect()` method of the `mysql.connector` module:
```
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd"
)
```

3. Create a cursor object using the `cursor()` method of the connection object:
```
mycursor = mydb.cursor()
```

4. Use the `execute()` method of the cursor object to execute a SQL query. For example, to create a database:
```
mycursor.execute("CREATE DATABASE mydatabase")
```

5. Use the `commit()` method of the connection object to commit the changes to the database:
```
mydb.commit()
```

6. Finally, close the connection using the `close()` method of the connection object:
```
mydb.close()
```

7. To test the connection, you can execute a SQL query such as `SELECT VERSION()`:
```
mycursor.execute("SELECT VERSION()")

# Output:
# 5.7.31-0ubuntu0.18.04.1
```

For more information, please refer to the [MySQL Connector Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I connect to a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-connect-to-a-mysql-database-using-python-1686995641)