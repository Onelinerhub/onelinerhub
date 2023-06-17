# How do I use Python to query MySQL with multiple conditions?
// plain

Using Python to query MySQL with multiple conditions is easy and straightforward. The following example code shows how to do this:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s AND name = %s"
adr = ("Park Lane 38", "John")

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

```

The output of the above code is:

```
('John', 'Park Lane 38')
```

The code consists of the following parts:

1. `import mysql.connector`: This is used to import the MySQL Connector Python module in order to connect to a MySQL database.

2. `mydb = mysql.connector.connect()`: This line of code is used to create a connection to the MySQL database.

3. `mycursor = mydb.cursor()`: This line of code is used to create a cursor object which will be used to execute the SQL query.

4. `sql = "SELECT * FROM customers WHERE address = %s AND name = %s"`: This line of code is used to define the SQL query. The `%s` is used as a placeholder for the values which will be passed as parameters to the query.

5. `adr = ("Park Lane 38", "John")`: This line of code is used to define the values which will be passed as parameters to the SQL query.

6. `mycursor.execute(sql, adr)`: This line of code is used to execute the SQL query with the parameters specified.

7. `myresult = mycursor.fetchall()`: This line of code is used to fetch all the rows from the result set of the query.

8. `for x in myresult: print(x)`: This line of code is used to iterate through the result set and print out the values.

For more information on using Python to query MySQL with multiple conditions, please refer to the following links:

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)

onelinerhub: [How do I use Python to query MySQL with multiple conditions?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-query-mysql-with-multiple-conditions)