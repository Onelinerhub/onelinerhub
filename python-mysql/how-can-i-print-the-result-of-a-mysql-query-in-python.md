# How can I print the result of a MySQL query in Python?
// plain

To print the result of a MySQL query in Python, you can use the `fetchall()` method of the `cursor` object. This method returns a list of tuples containing the results of the query. The example code below shows how to use `fetchall()` to print the result of a SELECT query:

```
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)

# Create cursor
mycursor = mydb.cursor()

# Execute query
mycursor.execute("SELECT * FROM customers")

# Fetch and print result
result = mycursor.fetchall()
print(result)
```

## Output example

```
[(1, 'John', 'Highway 21'), (2, 'Peter', 'Lowstreet 4'), (3, 'Amy', 'Apple st 652')]
```

The code above consists of the following parts:

1. Import the `mysql.connector` module.
2. Connect to the MySQL database.
3. Create a cursor object.
4. Execute the query.
5. Use the `fetchall()` method to fetch the result.
6. Print the result.

## Helpful links

- [MySQL Connector/Python Tutorial](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
- [MySQL Connector/Python Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How can I print the result of a MySQL query in Python?](https://onelinerhub.com/python-mysql/how-can-i-print-the-result-of-a-mysql-query-in-python)