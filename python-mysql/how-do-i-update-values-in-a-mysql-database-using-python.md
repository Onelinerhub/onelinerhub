# How do I update values in a MySQL database using Python?
// plain

Updating values in a MySQL database using Python is a relatively straightforward process. The following example code shows how to update a value in a MySQL database using Python:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
```

## Output example

```
1 record(s) affected
```

The code above consists of the following parts:

1. Importing the *mysql.connector* module.
2. Connecting to the database using the *mysql.connector.connect()* function.
3. Creating a cursor object using the *mydb.cursor()* method.
4. Creating an SQL query to update the value in the database.
5. Executing the query using the *mycursor.execute()* method.
6. Committing the changes to the database using the *mydb.commit()* method.
7. Printing the number of records affected with the *mycursor.rowcount* property.

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)
- [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql.asp)

onelinerhub: [How do I update values in a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-update-values-in-a-mysql-database-using-python)