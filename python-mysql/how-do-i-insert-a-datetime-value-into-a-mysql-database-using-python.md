# How do I insert a datetime value into a MySQL database using Python?
// plain

To insert a datetime value into a MySQL database using Python, use the `MySQL Connector/Python` library. The following example code creates a connection to a MySQL database, inserts a datetime value, and then prints the value in the database:

```
import mysql.connector

# Create connection to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

# Create cursor object
mycursor = mydb.cursor()

# Create SQL statement
sql = "INSERT INTO customers (name, datetime_field) VALUES (%s, %s)"
val = ("John", "2020-02-20 10:45:00")

# Execute SQL statement
mycursor.execute(sql, val)

# Commit changes to database
mydb.commit()

# Print the inserted datetime value
print(mycursor.rowcount, "record inserted.")

# Print the value from the database
sql = "SELECT datetime_field FROM customers WHERE name=%s"
val = ("John",)
mycursor.execute(sql, val)
result = mycursor.fetchone()
print("Datetime value in database:", result[0])
```

## Output example

```
1 record inserted.
Datetime value in database: 2020-02-20 10:45:00
```

The code consists of the following parts:

1. Import the `mysql.connector` library.
2. Create a connection to the MySQL database.
3. Create a cursor object.
4. Create a SQL statement to insert the datetime value into the database.
5. Execute the SQL statement.
6. Commit the changes to the database.
7. Print the number of records inserted.
8. Create a SQL statement to select the datetime value from the database.
9. Execute the SQL statement.
10. Fetch the result.
11. Print the datetime value from the database.

## Helpful links

- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL INSERT Statement](https://www.w3schools.com/sql/sql_insert.asp)

onelinerhub: [How do I insert a datetime value into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-insert-a-datetime-value-into-a-mysql-database-using-python)