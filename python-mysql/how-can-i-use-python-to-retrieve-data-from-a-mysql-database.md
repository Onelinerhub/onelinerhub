# How can I use Python to retrieve data from a MySQL database?
// plain

To use Python to retrieve data from a MySQL database, you can use the `MySQL Connector/Python` library. Below is an example code block to connect to a MySQL database and retrieve the data:

```python
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password"
)

# Create a cursor
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT * FROM customers")

# Retrieve the results
myresult = mycursor.fetchall()

# Print the results
for x in myresult:
  print(x)
```

The code above consists of the following parts:
1. Import the `mysql.connector` library
2. Connect to the database
3. Create a cursor
4. Execute a query
5. Retrieve the results
6. Print the results

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How can I use Python to retrieve data from a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-retrieve-data-from-a-mysql-database)