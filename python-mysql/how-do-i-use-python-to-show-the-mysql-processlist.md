# How do I use Python to show the MySQL processlist?
// plain

Using Python to show the MySQL processlist is a simple task.

First, you need to import the `mysql.connector` library.

```python
import mysql.connector
```

Then, create a connection to the MySQL server.

```python
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)
```

Once the connection is established, you can create a cursor object and execute the `SHOW PROCESSLIST` command.

```python
mycursor = mydb.cursor()

mycursor.execute("SHOW PROCESSLIST")

for x in mycursor:
  print(x)
```

The output of the above code will be a list of all the processes running on the MySQL server.

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL SHOW PROCESSLIST Syntax](https://dev.mysql.com/doc/refman/8.0/en/show-processlist.html)

onelinerhub: [How do I use Python to show the MySQL processlist?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-show-the-mysql-processlist)