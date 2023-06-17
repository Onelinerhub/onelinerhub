# How do I use Python and MySQL to get the number of rows?
// plain

Using Python and MySQL to get the number of rows is very easy. The following example code will illustrate how to do this:

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

# Create a cursor
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT * FROM table_name")

# Get the number of rows
num_rows = mycursor.rowcount

# Print the number of rows
print(num_rows)
```

## Output example

```
50
```

The code consists of the following parts:
1. Import the `mysql.connector` module.
2. Connect to the database.
3. Create a cursor.
4. Execute a query.
5. Get the number of rows.
6. Print the number of rows.

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I use Python and MySQL to get the number of rows?](https://onelinerhub.com/python-mysql/how-do-i-use-python-and-mysql-to-get-the-number-of-rows)