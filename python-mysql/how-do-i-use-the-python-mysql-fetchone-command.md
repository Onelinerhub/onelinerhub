# How do I use the Python MySQL fetchone command?
// plain

The Python MySQL fetchone command allows you to retrieve a single row from a MySQL table query result. It is used to fetch the next row of a query result set and return a single tuple, or None if no more rows are available.

## Example

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)

```
## Output example

```
('John', 'Highway 21')
```

The code above establishes a connection to a MySQL database, creates a cursor object, executes a SQL query to select all records from the customers table, and then uses the fetchone() method to retrieve a single row from the result set.

## Code explanation

- `import mysql.connector`: imports the MySQL Connector Python module.
- `mydb = mysql.connector.connect(host="localhost", user="user", passwd="passwd", database="mydatabase")`: establishes a connection to a MySQL database.
- `mycursor = mydb.cursor()`: creates a cursor object.
- `mycursor.execute("SELECT * FROM customers")`: executes a SQL query to select all records from the customers table.
- `myresult = mycursor.fetchone()`: uses the fetchone() method to retrieve a single row from the result set.
- `print(myresult)`: prints the record retrieved from the result set.

## Helpful links
- [MySQL Connector Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Cursor fetchone() Method](https://www.w3schools.com/python/ref_mysql_fetchone.asp)

onelinerhub: [How do I use the Python MySQL fetchone command?](https://onelinerhub.com/python-mysql/how-do-i-use-the-python-mysql-fetchone-command)