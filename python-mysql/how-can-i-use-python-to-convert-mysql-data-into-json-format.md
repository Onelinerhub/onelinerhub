# How can I use Python to convert MySQL data into JSON format?
// plain

To convert MySQL data into JSON format using Python, you can use the `json` library and `mysql.connector` library. Below is an example of how this can be done:

```
import mysql.connector
import json

# Establish connection to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="yourdatabasename"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query
query = "SELECT * FROM customers"
mycursor.execute(query)

# Fetch all the rows
rows = mycursor.fetchall()

# Convert the rows into JSON
json_data = json.dumps(rows)

# Print the JSON
print(json_data)
```

## Output example

```
[["John", "Highway 21"], ["Amy", "Mountain 21"]]
```

The code above consists of the following parts:
1. `import mysql.connector` and `import json` - imports the necessary libraries.
2. `mydb = mysql.connector.connect()` - establishes a connection to the MySQL database.
3. `mycursor = mydb.cursor()` - creates a cursor object.
4. `query = "SELECT * FROM customers"` - creates a query to select all data from the `customers` table.
5. `mycursor.execute(query)` - executes the query.
6. `rows = mycursor.fetchall()` - fetches all the rows from the table.
7. `json_data = json.dumps(rows)` - converts the rows into JSON.
8. `print(json_data)` - prints the JSON data.

## Helpful links
- [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/)
- [JSON in Python](https://www.w3schools.com/python/python_json.asp)

onelinerhub: [How can I use Python to convert MySQL data into JSON format?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-convert-mysql-data-into-json-format)