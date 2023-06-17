# How can I get the table headers in a MySQL database using Python?
// plain

You can get the table headers in a MySQL database using Python by using the `cursor.description` method. This method returns a list of 7-item tuples containing column information such as name, type, display size, internal size, precision, scale, and nullability. An example is shown below:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

print(mycursor.description)
```

## Output example

```
(('id', 3, None, 11, 11, 0, False), ('name', 253, None, 255, 255, 0, False), ('address', 253, None, 255, 255, 0, False))
```

## Code explanation


1. `import mysql.connector`: imports the mysql.connector module to use for connecting to the database.
2. `mydb = mysql.connector.connect(...)`: establishes a connection to the database.
3. `mycursor = mydb.cursor()`: creates a cursor object to execute SQL queries.
4. `mycursor.execute("SELECT * FROM customers")`: executes the SQL query to select all records from the customers table.
5. `print(mycursor.description)`: prints out the table headers in the form of a list of 7-item tuples.

## Helpful links

- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Cursor](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

onelinerhub: [How can I get the table headers in a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-get-the-table-headers-in-a-mysql-database-using-python)