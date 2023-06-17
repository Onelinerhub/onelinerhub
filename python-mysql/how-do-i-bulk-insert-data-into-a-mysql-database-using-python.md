# How do I bulk insert data into a MySQL database using Python?
// plain

The following example demonstrates how to bulk insert data into a MySQL database using Python.

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('John', 'Highway 21'),
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

```
## Output example

```
14 record inserted.
```

The code consists of the following parts:
1. Importing the mysql.connector module.
2. Connecting to the database.
3. Creating a cursor object.
4. Creating a SQL query.
5. Creating a list of values to be inserted.
6. Executing the query.
7. Committing the changes to the database.
8. Printing the number of rows affected.

## Helpful links
1. [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
2. [MySQL Connector/Python Tutorial](https://www.w3schools.com/python/python_mysql_getstarted.asp)

onelinerhub: [How do I bulk insert data into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-bulk-insert-data-into-a-mysql-database-using-python)