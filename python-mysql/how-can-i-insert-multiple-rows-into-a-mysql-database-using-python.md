# How can I insert multiple rows into a MySQL database using Python?
// plain

To insert multiple rows into a MySQL database using Python, you can use the executemany() method of the MySQLCursor object. This method takes a list of tuples containing the data for each row to be inserted.

For example:

```
import mysql.connector

# Connect to the database
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


`14 records inserted.`

## Code explanation


1. `import mysql.connector` - import the MySQL Connector Python module
2. `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword", database="mydatabase")` - connect to the database
3. `mycursor = mydb.cursor()` - create a cursor object
4. `sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"` - define an SQL query
5. `val = [('John', 'Highway 21'),('Peter', 'Lowstreet 4'),...('Viola', 'Sideway 1633')]` - create a list of tuples containing the data for each row to be inserted
6. `mycursor.executemany(sql, val)` - execute the SQL query using the executemany() method
7. `mydb.commit()` - commit the changes to the database
8. `print(mycursor.rowcount, "record inserted.")` - print the number of rows inserted

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How can I insert multiple rows into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-insert-multiple-rows-into-a-mysql-database-using-python)