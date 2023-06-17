# How do I execute a batch insert into a MySQL database using Python?
// plain

To execute a batch insert into a MySQL database using Python, you need to do the following:

1. Establish a connection to the database:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()
```

2. Create a list of values to insert:
```
sql_values = [
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
```

3. Create the SQL query:
```
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
```

4. Execute the query using the `executemany()` method:
```
mycursor.executemany(sql, sql_values)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```
## Output example

```
14 records inserted.
```

5. Close the connection:
```
mycursor.close()
mydb.close()
```

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How do I execute a batch insert into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-execute-a-batch-insert-into-a-mysql-database-using-python)