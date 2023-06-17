# How can I use Python to connect to a MySQL database and generate HTML output?
// plain

To connect to a MySQL database and generate HTML output using Python, you can use the [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/).

First, you will need to install the MySQL Connector/Python by running the command `pip install mysql-connector-python`.

Once installed, you can establish a connection to the database using the following code block:
```python
import mysql.connector

# Establish a connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

# Create a cursor object
mycursor = mydb.cursor()
```

Once you have established a connection to the database, you can use the cursor object to execute queries and retrieve results. For example, to retrieve data from a table called 'customers':
```python
# Execute a query
mycursor.execute("SELECT * FROM customers")

# Retrieve the results
myresult = mycursor.fetchall()

# Print the results
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

Once you have retrieved the data, you can generate HTML output by looping through the results and constructing HTML elements. For example:
```python
# Construct HTML table
html_output = "<table>"
for x in myresult:
  html_output += "<tr><td>{0}</td><td>{1}</td></tr>".format(x[0], x[1])
html_output += "</table>"

# Print HTML output
print(html_output)
```

## Output example

```
<table><tr><td>John</td><td>Highway 21</td></tr><tr><td>Peter</td><td>Lowstreet 4</td></tr><tr><td>Amy</td><td>Apple st 652</td></tr><tr><td>Hannah</td><td>Mountain 21</td></tr></table>
```

This example code demonstrates how to use Python to connect to a MySQL database and generate HTML output.

onelinerhub: [How can I use Python to connect to a MySQL database and generate HTML output?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-connect-to-a-mysql-database-and-generate-html-output)