# How can I get the row count of a MySQL table using Python?
// plain

You can get the row count of a MySQL table using Python by executing a SQL query with the `COUNT()` function.

## Example code

```
#import mysql.connector
import mysql.connector

#connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

#create cursor
mycursor = mydb.cursor()

#create sql query
sql = "SELECT COUNT(*) FROM customers"

#execute sql query
mycursor.execute(sql)

#fetch result
myresult = mycursor.fetchone()

#print result
print(myresult)
```
## Output example

```
(50,)
```

## Code explanation

1. `import mysql.connector` - imports the mysql.connector module.
2. `mydb = mysql.connector.connect()` - connects to the database.
3. `mycursor = mydb.cursor()` - creates a cursor to the database.
4. `sql = "SELECT COUNT(*) FROM customers"` - creates a SQL query with the `COUNT()` function.
5. `mycursor.execute(sql)` - executes the SQL query.
6. `myresult = mycursor.fetchone()` - fetches the result of the query.
7. `print(myresult)` - prints the result.

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)
- [MySQL COUNT() Function](https://www.w3schools.com/sql/sql_count_avg_sum.asp)

onelinerhub: [How can I get the row count of a MySQL table using Python?](https://onelinerhub.com/python-mysql/how-can-i-get-the-row-count-of-a-mysql-table-using-python)