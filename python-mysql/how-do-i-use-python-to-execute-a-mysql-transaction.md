# How do I use Python to execute a MySQL transaction?
// plain

Using Python to execute a MySQL transaction is a relatively straightforward process. The most basic approach is to use the `MySQLdb` library as follows:

```python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","user","password","database" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO table_name (field1, field2) VALUES ('%s', '%s')" % (value1, value2)

# Execute the SQL command
cursor.execute(sql)

# Commit your changes in the database
db.commit()

# disconnect from server
db.close()
```

This code will open a connection to the MySQL database, create a cursor object, prepare an SQL query to insert a record, execute the query, commit the changes, and then close the connection.

## Code explanation


1. `import MySQLdb` - this imports the `MySQLdb` library which provides the necessary functions to connect to and interact with the MySQL database.
2. `db = MySQLdb.connect("localhost","user","password","database" )` - this creates a connection to the MySQL database. The parameters are the host, user, password, and database name.
3. `cursor = db.cursor()` - this creates a cursor object which is used to interact with the database.
4. `sql = "INSERT INTO table_name (field1, field2) VALUES ('%s', '%s')" % (value1, value2)` - this prepares an SQL query to insert a record into the database.
5. `cursor.execute(sql)` - this executes the SQL query.
6. `db.commit()` - this commits the changes to the database.
7. `db.close()` - this closes the connection to the database.

For more information, see the [MySQLdb documentation](https://mysqlclient.readthedocs.io/user_guide.html) and the [MySQL Tutorial](https://www.mysqltutorial.org/).

onelinerhub: [How do I use Python to execute a MySQL transaction?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-execute-a-mysql-transaction)