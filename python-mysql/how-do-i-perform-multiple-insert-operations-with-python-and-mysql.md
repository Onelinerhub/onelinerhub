# How do I perform multiple insert operations with Python and MySQL?
// plain

To perform multiple insert operations with Python and MySQL, you can use the `executemany()` method of the MySQL cursor object. This method accepts a parameter which is a list of tuples, each tuple containing the data to be inserted into one row. The following example code shows how to use this method to insert multiple rows into a table:

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

print(mycursor.rowcount, "was inserted.")
```

## Output example

```
14 was inserted.
```

The code above:

1. Imports the `mysql.connector` package.
2. Creates a connection to the MySQL database.
3. Creates a cursor object.
4. Defines the SQL query to be executed.
5. Defines a list of tuples containing the data to be inserted.
6. Executes the query using the `executemany()` method.
7. Commits the changes to the database.

## Helpful links

1. [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
2. [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)

onelinerhub: [How do I perform multiple insert operations with Python and MySQL?](https://onelinerhub.com/python-mysql/how-do-i-perform-multiple-insert-operations-with-python-and-mysql)