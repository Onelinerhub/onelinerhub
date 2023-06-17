# How do I insert NULL values into a MySQL table using Python?
// plain

To insert NULL values into a MySQL table using Python, you can use the [MySQL Connector Python library](https://dev.mysql.com/doc/connector-python/en/). The following code block shows an example of how to insert a NULL value into a MySQL table using the library:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = (None, "California")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

The output of the above code will be `1 record inserted.`

The code is broken down into the following parts:

1. Importing the `mysql.connector` library to connect to the MySQL database.
2. Establishing a connection to the MySQL database.
3. Creating a cursor object to execute queries and commands.
4. Writing a SQL query to insert a NULL value into the customers table.
5. Executing the query.
6. Committing the changes to the database.
7. Printing the number of records inserted.

For more information, please refer to the [MySQL Connector Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I insert NULL values into a MySQL table using Python?](https://onelinerhub.com/python-mysql/how-do-i-insert-null-values-into-a-mysql-table-using-python)