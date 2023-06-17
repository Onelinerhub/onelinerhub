# How can I insert data into a MySQL database using Python?
// plain

To insert data into a MySQL database using Python, you can use the `mysql.connector` library. The following example code shows how to connect to a MySQL database, create a table, and insert data into the table.

```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password"
)

# Create a cursor
mycursor = mydb.cursor()

# Create a table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Insert data into the table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

# Commit the changes to the database
mydb.commit()

# Print the number of rows affected
print(mycursor.rowcount, "record inserted.")
```
## Output example

1 record inserted.

## Code explanation

1. Import the `mysql.connector` library - `import mysql.connector`
2. Connect to the database - `mydb = mysql.connector.connect(host="localhost", user="user", passwd="password")`
3. Create a cursor - `mycursor = mydb.cursor()`
4. Create a table - `mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")`
5. Insert data into the table - `sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"`
6. Execute the SQL query using the cursor - `mycursor.execute(sql, val)`
7. Commit the changes to the database - `mydb.commit()`

## Helpful links
1. [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql.asp)
2. [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)

onelinerhub: [How can I insert data into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-insert-data-into-a-mysql-database-using-python)