# How can I use the "LIKE" operator with Python and MySQL?
// plain

The `LIKE` operator is used to search for a specific pattern in a column of a MySQL table using Python. It can be used in the `SELECT` statement to retrieve rows from a table based on a certain pattern.

## Example code

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

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

The code above is composed of these parts:
1. `import mysql.connector` - imports the MySQL Connector Python module which allows Python to connect to a MySQL database.
2. `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")` - establishes a connection to the MySQL database.
3. `mycursor = mydb.cursor()` - creates a cursor object which is used to execute SQL commands.
4. `sql = "SELECT * FROM customers WHERE address LIKE '%way%'"` - creates a SQL query which selects all rows from the `customers` table where the `address` column contains the pattern `way`.
5. `mycursor.execute(sql)` - executes the SQL query.
6. `myresult = mycursor.fetchall()` - retrieves the results of the SQL query.
7. `for x in myresult: print(x)` - prints the results of the SQL query.

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL LIKE Operator](https://www.w3schools.com/sql/sql_like.asp)

onelinerhub: [How can I use the "LIKE" operator with Python and MySQL?](https://onelinerhub.com/python-mysql/how-can-i-use-the--like--operator-with-python-and-mysql)