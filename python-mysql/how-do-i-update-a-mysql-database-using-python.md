# How do I update a MySQL database using Python?
// plain

To update a MySQL database using Python, you can use the `MySQL Connector/Python` library. This library provides an easy way to access and manipulate MySQL databases. Here is an example of how to update a record in a MySQL database using Python:

```python
# Import the MySQL Connector/Python library
import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Construct an UPDATE statement
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# Execute the statement
mycursor.execute(sql)

# Commit the changes to the database
mydb.commit()

# Print number of rows updated
print(mycursor.rowcount, "record(s) updated")
```

## Output example

```
1 record(s) updated
```

The code above consists of the following parts:
1. Import the `MySQL Connector/Python` library
2. Establish a connection to the MySQL database
3. Create a cursor object
4. Construct an `UPDATE` statement
5. Execute the statement
6. Commit the changes to the database
7. Print number of rows updated

For more information, refer to the [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I update a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-update-a-mysql-database-using-python)