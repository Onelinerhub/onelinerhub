# How do I use Python to update multiple columns in a MySQL database?
// plain

You can use Python to update multiple columns in a MySQL database by using the `UPDATE` command. For example, the following code will update the `name` and `age` columns of the `users` table:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE users SET name = 'John', age = '32' WHERE name = 'Peter'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
```

## Output example

```
1 record(s) affected
```

#### Explanation of the code:
1. `import mysql.connector`: This imports the MySQL Connector Python module in order to establish a connection to the database.
2. `mydb = mysql.connector.connect()`: This establishes a connection to the database using the credentials provided as parameters.
3. `mycursor = mydb.cursor()`: This creates a cursor object which is used to execute the SQL statements.
4. `sql = "UPDATE users SET name = 'John', age = '32' WHERE name = 'Peter'"`: This is the SQL statement used to update the `name` and `age` columns of the `users` table.
5. `mycursor.execute(sql)`: This executes the SQL statement.
6. `mydb.commit()`: This commits the changes to the database.
7. `print(mycursor.rowcount, "record(s) affected")`: This prints the number of records affected by the query.

#### ## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL UPDATE Statement](https://www.w3schools.com/sql/sql_update.asp)

onelinerhub: [How do I use Python to update multiple columns in a MySQL database?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-update-multiple-columns-in-a-mysql-database)