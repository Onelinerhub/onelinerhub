# How do I use a SELECT statement in Python to query a MySQL database?
// plain

In order to use a SELECT statement in Python to query a MySQL database, the following steps should be taken:

1. Establish a connection to the MySQL database using the `mysql.connector` library:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)
```

2. Create a cursor object by calling the `cursor()` method of the connection object:
```
mycursor = mydb.cursor()
```

3. Use the `execute()` method of the cursor object to execute the SELECT statement:
```
mycursor.execute("SELECT * FROM customers")
```

4. Fetch all the records from the SELECT statement using the `fetchall()` method of the cursor object:
```
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```
## Output example

```
('John', 'Highway 21')
('Amy', 'Mountain 21')
('Hannah', 'Valley 345')
```

5. Close the cursor and the connection to the database using the `close()` method of the cursor and connection objects respectively:
```
mycursor.close()
mydb.close()
```

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/index.html)
- [MySQL SELECT Statement](https://www.w3schools.com/sql/sql_select.asp)

onelinerhub: [How do I use a SELECT statement in Python to query a MySQL database?](https://onelinerhub.com/python-mysql/how-do-i-use-a-select-statement-in-python-to-query-a-mysql-database)