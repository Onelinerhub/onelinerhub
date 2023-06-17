# How do I use a cursor to interact with a MySQL database in Python?
// plain

Using a cursor to interact with a MySQL database in Python is easy and efficient. To do this, you'll need to import the MySQL Connector library for Python.

```
import mysql.connector
```

Once the library is imported, you can create a connection to the MySQL database using the `connect()` method.

```
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)
```

Next, you can create a cursor object from the connection using the `cursor()` method.

```
mycursor = mydb.cursor()
```

After that, you can use the cursor to execute SQL queries. For example, you can use the `execute()` method to create a table.

```
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
```

Finally, you can use the `fetchall()` method to get the results of a query.

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

## Code explanation

- `import mysql.connector`: This imports the MySQL Connector library for Python.
- `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")`: This creates a connection to the MySQL database using the `connect()` method.
- `mycursor = mydb.cursor()`: This creates a cursor object from the connection using the `cursor()` method.
- `mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")`: This uses the `execute()` method to create a table.
- `mycursor.execute("SELECT * FROM customers")`: This uses the `execute()` method to execute a query.
- `myresult = mycursor.fetchall()`: This uses the `fetchall()` method to get the results of a query.
- `for x in myresult: print(x)`: This prints the results of the query.

## Helpful links
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Cursor](https://pynative.com/python-mysql-cursor-objects/)

onelinerhub: [How do I use a cursor to interact with a MySQL database in Python?](https://onelinerhub.com/python-mysql/how-do-i-use-a-cursor-to-interact-with-a-mysql-database-in-python)