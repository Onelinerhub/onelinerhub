# How do I get the ID of the inserted row in a MySQL database using Python?
// plain

The ID of the inserted row in a MySQL database can be obtained using Python with the help of the `mysql.connector` library. Here is an example code block demonstrating how to do this:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
```

The output of the code above would be:

```
1 record inserted, ID: 8
```

The code consists of the following parts:

1. Importing the `mysql.connector` library.
2. Establishing a connection to the MySQL database.
3. Creating a cursor object.
4. Writing an SQL query to insert a row into the database.
5. Executing the query with the values to be inserted.
6. Committing the changes to the database.
7. Printing the ID of the inserted row.

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Reference Manual](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

onelinerhub: [How do I get the ID of the inserted row in a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-get-the-id-of-the-inserted-row-in-a-mysql-database-using-python)