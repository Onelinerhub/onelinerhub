# How do I use the Python MySQL fetchmany method?
// plain

The Python MySQL fetchmany method is used to retrieve a number of rows from a cursor object. This method takes an argument which specifies the number of rows to be retrieved. It returns a list of tuples, with each tuple representing a row.

For example:
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

myresult = mycursor.fetchmany(3)

for x in myresult:
  print(x)
```
## Output example

```
('John', 'Highway 21')
('Peter', 'Lowstreet 4')
('Amy', 'Apple st 652')
```

1. `import mysql.connector` - This imports the MySQL Connector Python module.
2. `mydb = mysql.connector.connect(host="localhost", user="user", passwd="passwd", database="mydatabase")` - This establishes a connection to the database.
3. `mycursor = mydb.cursor()` - This creates a cursor object.
4. `mycursor.execute("SELECT * FROM customers")` - This executes a SQL query to select all records from the customers table.
5. `myresult = mycursor.fetchmany(3)` - This fetches the next 3 records from the cursor object.
6. `for x in myresult:` - This iterates through the result set and prints each row.
7. `print(x)` - This prints the row.

## Helpful links

- [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql.asp)
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)

onelinerhub: [How do I use the Python MySQL fetchmany method?](https://onelinerhub.com/python-mysql/how-do-i-use-the-python-mysql-fetchmany-method)