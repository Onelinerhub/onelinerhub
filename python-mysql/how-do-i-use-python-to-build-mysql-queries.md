# How do I use Python to build MySQL queries?
// plain

Using Python to build MySQL queries is a great way to make sure your queries are well-constructed and accurate. Here is an example of how to do it:

```
#import the mysql.connector library/module
import mysql.connector

#establish connection to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

#create cursor
mycursor = mydb.cursor()

#build query
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

#execute query
mycursor.execute(sql, val)

#commit changes to database
mydb.commit()

#print number of records inserted
print(mycursor.rowcount, "record inserted.")
```

## Output example


```
1 record inserted.
```

The code above can be broken down as follows:

1. `import mysql.connector` - imports the mysql.connector library/module so you can use its functions.
2. `mydb = mysql.connector.connect()` - establishes a connection to the MySQL database using the parameters provided.
3. `mycursor = mydb.cursor()` - creates a cursor object which allows you to execute queries.
4. `sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"` - builds a SQL query to insert data into the customers table.
5. `val = ("John", "Highway 21")` - specifies the values to be inserted into the customers table.
6. `mycursor.execute(sql, val)` - executes the query with the provided values.
7. `mydb.commit()` - commits the changes to the database.
8. `print(mycursor.rowcount, "record inserted.")` - prints the number of records inserted.

For more information on using Python to build MySQL queries, check out the [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How do I use Python to build MySQL queries?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-build-mysql-queries)