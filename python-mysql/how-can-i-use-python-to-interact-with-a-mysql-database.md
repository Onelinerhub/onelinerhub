# How can I use Python to interact with a MySQL database?
// plain

Python can be used to interact with a MySQL database using the MySQL Connector/Python. This library provides an interface for connecting to a MySQL server and executing SQL statements.

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

mycursor.execute("SELECT * FROM customers")

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

The code above:
- Imports the `mysql.connector` library (1)
- Connects to a MySQL database (2)
- Creates a cursor object (3)
- Executes an SQL statement to select all records from the `customers` table (4)
- Fetches all the results of the query (5)
- Prints out each row of the result (6)

## Helpful links
- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Tutorial](https://www.mysqltutorial.org/python-mysql/)

onelinerhub: [How can I use Python to interact with a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-interact-with-a-mysql-database)