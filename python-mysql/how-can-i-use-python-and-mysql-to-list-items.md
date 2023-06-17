# How can I use Python and MySQL to list items?
// plain

Python and MySQL can be used to list items in a variety of ways. For example, the following code can be used to list all the items in a table in a MySQL database:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM items")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

## Output example

```
('item1', 'description1')
('item2', 'description2')
('item3', 'description3')
```

The code consists of the following parts:
1. `import mysql.connector`: This imports the MySQL Connector Python module, which is used to connect to a MySQL database.
2. `mydb = mysql.connector.connect()`: This creates a connection to the MySQL database using the provided credentials.
3. `mycursor = mydb.cursor()`: This creates a cursor object that can be used to execute SQL queries.
4. `mycursor.execute("SELECT * FROM items")`: This executes a SQL query to select all the items from the "items" table.
5. `myresult = mycursor.fetchall()`: This fetches all the results from the query and stores them in a variable.
6. `for x in myresult: print(x)`: This loop iterates through the results and prints them.

For more information, please refer to the following links:
- [MySQL Connector Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL SELECT Statement Documentation](https://dev.mysql.com/doc/refman/8.0/en/select.html)

onelinerhub: [How can I use Python and MySQL to list items?](https://onelinerhub.com/python-mysql/how-can-i-use-python-and-mysql-to-list-items)