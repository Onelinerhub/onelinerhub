# How do I write a Python MySQL query?
// plain

Writing a Python MySQL query is simple and straightforward. To begin, you will need to import the MySQL Connector module and create a connection to the database.

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()
```

Once connected, you can execute SQL queries on the database. For example, to select all records from a table, you can use the following command:

```python
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

The output of the above code will be a list of all records in the customers table.

You can also use parameters in your queries. For example, to select all records from a table where the name is "John", you can use the following command:

```python
sql = "SELECT * FROM customers WHERE name = %s"
name = ("John", )

mycursor.execute(sql, name)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

The output of the above code will be a list of all records in the customers table where the name is "John".

To learn more about writing Python MySQL queries, please refer to the following links:

- [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql_getstarted.asp)
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)

onelinerhub: [How do I write a Python MySQL query?](https://onelinerhub.com/python-mysql/how-do-i-write-a-python-mysql-query)