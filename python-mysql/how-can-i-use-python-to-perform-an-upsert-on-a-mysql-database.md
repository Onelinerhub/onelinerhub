# How can I use Python to perform an upsert on a MySQL database?
// plain

Upsert is a combination of update and insert operations in a database. To perform an upsert in a MySQL database with Python, we can use the [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) library. The following example code will perform an upsert on a table named `my_table`:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO my_table (name, address) VALUES (%s, %s) ON DUPLICATE KEY UPDATE address = %s"
val = ("John", "Highway 21", "Valley 345")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

This code will output: `1 record inserted.`

The code consists of the following parts:

1. Importing the MySQL Connector/Python library: `import mysql.connector`
2. Connecting to the database: `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword", database="mydatabase")`
3. Creating a cursor object: `mycursor = mydb.cursor()`
4. Preparing the SQL query: `sql = "INSERT INTO my_table (name, address) VALUES (%s, %s) ON DUPLICATE KEY UPDATE address = %s"`
5. Executing the query: `mycursor.execute(sql, val)`
6. Committing the changes to the database: `mydb.commit()`
7. Printing the result: `print(mycursor.rowcount, "record inserted.")`

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I use Python to perform an upsert on a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-python-to-perform-an-upsert-on-a-mysql-database)