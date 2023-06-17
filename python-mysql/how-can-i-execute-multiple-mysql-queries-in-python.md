# How can I execute multiple MySQL queries in Python?
// plain

You can execute multiple MySQL queries in Python using the `MySQL Connector/Python` library.

## Example code

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Peter", "Lowstreet 4")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```
## Output example
 `2 record inserted.`

## Code explanation

- `import mysql.connector`: imports the `MySQL Connector/Python` library
- `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")`: connects to the MySQL database using the provided credentials
- `mycursor = mydb.cursor()`: creates a cursor object
- `sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"`: creates a SQL query string
- `val = ("John", "Highway 21")`: creates a tuple containing the values to be inserted into the database
- `mycursor.execute(sql, val)`: executes the SQL query using the provided values
- `mydb.commit()`: commits the changes to the database
- `print(mycursor.rowcount, "record inserted.")`: prints the number of records inserted

## Helpful links
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Cursor Class](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

onelinerhub: [How can I execute multiple MySQL queries in Python?](https://onelinerhub.com/python-mysql/how-can-i-execute-multiple-mysql-queries-in-python)