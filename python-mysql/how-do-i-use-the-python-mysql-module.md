# How do I use the Python MySQL module?
// plain

The Python MySQL module is a library that allows Python programs to access a MySQL database. To use the module, you must first install it using the command `pip install mysql-connector-python`.

Once it is installed, you can use the module in your Python program by importing it.

```python
import mysql.connector
```

To connect to a database, you must first create a `MySQLConnection` object, which requires a few parameters such as the username, password, database name, and host.

```python
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)
```

Once the connection is established, you can use the `cursor()` method of the `MySQLConnection` object to create a `MySQLCursor` object. This object can be used to execute SQL queries, fetch results, and perform other database operations.

```python
mycursor = mydb.cursor()

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
('Michael', 'Valley 345')
('Sandy', 'Ocean blvd 2')
('Betty', 'Green Grass 1')
('Richard', 'Sky st 331')
('Susan', 'One way 98')
('Vicky', 'Yellow Garden 2')
('Ben', 'Park Lane 38')
('William', 'Central st 954')
('Chuck', 'Main Road 989')
('Viola', 'Sideway 1633')
```

For more information, you can refer to the [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I use the Python MySQL module?](https://onelinerhub.com/python-mysql/how-do-i-use-the-python-mysql-module)