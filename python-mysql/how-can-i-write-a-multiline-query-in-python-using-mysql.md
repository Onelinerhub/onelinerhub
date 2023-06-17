# How can I write a multiline query in Python using MySQL?
// plain

Writing a multiline query in Python using MySQL is a powerful way to execute multiple queries at once. It is done using the `executemany()` method of the `cursor` object. Here is an example of a multiline query in Python using MySQL:

```
# Import the MySQL connector
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="database"
)

# Create a cursor
cursor = db.cursor()

# Define the queries
query1 = "SELECT * FROM table1"
query2 = "SELECT * FROM table2"

# Create a list of queries
queries = [query1, query2]

# Execute the queries
cursor.executemany(query, queries)

# Fetch the results
results = cursor.fetchall()

# Print the results
print(results)
```

## Output example

```
[('value1', 'value2'), ('value3', 'value4')]
```

The code above consists of the following parts:
1. Import the MySQL connector - imports the mysql.connector module.
2. Connect to the database - connects to the database using the connect() method.
3. Create a cursor - creates a cursor object to execute queries.
4. Define the queries - defines the queries as strings.
5. Create a list of queries - creates a list of queries to be executed.
6. Execute the queries - uses the executemany() method to execute the queries.
7. Fetch the results - uses the fetchall() method to retrieve the results.
8. Print the results - prints the results to the console.

## Helpful links
- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Tutorial](https://www.w3schools.com/python/python_mysql_getstarted.asp)

onelinerhub: [How can I write a multiline query in Python using MySQL?](https://onelinerhub.com/python-mysql/how-can-i-write-a-multiline-query-in-python-using-mysql)