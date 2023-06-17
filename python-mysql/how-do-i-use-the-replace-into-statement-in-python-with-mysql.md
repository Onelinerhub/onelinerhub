# How do I use the REPLACE INTO statement in Python with MySQL?
// plain

The REPLACE INTO statement in Python with MySQL is used to insert a new row or replace an existing row in a table. It has the same syntax as the INSERT INTO statement, except that it replaces the existing row if the new row has the same primary key value.

## Example code

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "REPLACE INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

## Output example

```
1 record inserted.
```

## Code explanation

- `import mysql.connector`: imports the MySQL Connector Python module.
- `mydb = mysql.connector.connect()`: establishes a connection to the MySQL database.
- `mycursor = mydb.cursor()`: creates a cursor object.
- `sql = "REPLACE INTO customers (name, address) VALUES (%s, %s)"`: sets the SQL query string.
- `val = ("John", "Highway 21")`: sets the values to be inserted into the table.
- `mycursor.execute(sql, val)`: executes the SQL query.
- `mydb.commit()`: commits the changes to the database.
- `print(mycursor.rowcount, "record inserted.")`: prints the number of affected rows.

## Helpful links
- [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL REPLACE INTO Statement](https://www.w3schools.com/sql/sql_replace.asp)

onelinerhub: [How do I use the REPLACE INTO statement in Python with MySQL?](https://onelinerhub.com/python-mysql/how-do-i-use-the-replace-into-statement-in-python-with-mysql)