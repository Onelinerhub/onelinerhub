# How do I install and use the Python MySQL driver?
// plain

1. First, you need to install the Python MySQL driver. You can do this by using the pip package manager: `pip install mysql-connector-python`
2. Next, you need to import the driver into your Python code. You can do this by using the `import` statement: `import mysql.connector`
3. After you have imported the driver, you can create a connection to your MySQL database:

```
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd"
)
```

4. Once you have established a connection, you can create a cursor object to execute SQL statements:

```
mycursor = mydb.cursor()
```

5. You can now execute SQL statements using the `execute()` method:

```
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

## Output example

```
('John', 'Highway 21')
('Peter', 'Lowstreet 4')
('Amy', 'Apple st 652')
('Hannah', 'Mountain 21')
```

6. Finally, you can close the connection to your MySQL database using the `close()` method:

```
mydb.close()
```

7. For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I install and use the Python MySQL driver?](https://onelinerhub.com/python-mysql/how-do-i-install-and-use-the-python-mysql-driver)