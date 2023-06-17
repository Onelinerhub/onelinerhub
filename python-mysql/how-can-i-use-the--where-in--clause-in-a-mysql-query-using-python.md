# How can I use the "WHERE IN" clause in a MySQL query using Python?
// plain

The `WHERE IN` clause is a powerful clause used to filter the results of a query based on values in a specified list or subquery. This clause can be used in a MySQL query using Python by using the `execute()` method of the `cursor` object.

Here is an example of a MySQL query using Python with the `WHERE IN` clause:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address IN ('Valley 345', 'Park Lane 38')"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

```
This example will output the following:
```
('John', 'Doe', 'Park Lane 38')
('Mary', 'Moe', 'Valley 345')
```

The code can be broken down into the following parts:

1. `import mysql.connector`: This imports the `mysql.connector` module, which allows us to connect to a MySQL database.

2. `mydb = mysql.connector.connect()`: This creates a connection to the MySQL database.

3. `mycursor = mydb.cursor()`: This creates a cursor object, which allows us to execute SQL queries.

4. `sql = "SELECT * FROM customers WHERE address IN ('Valley 345', 'Park Lane 38')"`: This is the SQL query that uses the `WHERE IN` clause to filter the results based on the specified list of addresses.

5. `mycursor.execute(sql)`: This executes the SQL query.

6. `myresult = mycursor.fetchall()`: This fetches the results of the query and stores them in the `myresult` variable.

7. `for x in myresult:`: This is a `for` loop that iterates over each row in the `myresult` variable and prints the results.

## Helpful links

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL WHERE IN Clause](https://www.w3schools.com/sql/sql_in.asp)

onelinerhub: [How can I use the "WHERE IN" clause in a MySQL query using Python?](https://onelinerhub.com/python-mysql/how-can-i-use-the--where-in--clause-in-a-mysql-query-using-python)