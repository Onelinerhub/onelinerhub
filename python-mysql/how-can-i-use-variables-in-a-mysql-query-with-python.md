# How can I use variables in a MySQL query with Python?
// plain

Using variables in a MySQL query with Python can be done using the `MySQLdb` library.

An example of this is shown below:

```python
import MySQLdb

# Open database connection
db = MySQLdb.connect("hostname","username","password","database_name" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO table_name(column_1,column_2) VALUES (%s,%s)"

# Execute the SQL command
cursor.execute(sql, (variable_1,variable_2))

# Commit your changes in the database
db.commit()
```

In this example, we use the `MySQLdb` library to connect to a MySQL database. We then prepare a SQL query to insert a record into the database, with `%s` placeholders for the variables. The variables are then passed into the `cursor.execute()` method, and the changes are committed to the database.

The parts of the code are as follows:
* `import MySQLdb` - imports the `MySQLdb` library
* `db = MySQLdb.connect("hostname","username","password","database_name" )` - connects to the database
* `cursor = db.cursor()` - creates a cursor object
* `sql = "INSERT INTO table_name(column_1,column_2) VALUES (%s,%s)"` - prepares the SQL query
* `cursor.execute(sql, (variable_1,variable_2))` - executes the SQL query with the variables
* `db.commit()` - commits the changes to the database

## Helpful links
* [MySQLdb Documentation](https://mysqlclient.readthedocs.io/user_guide.html)
* [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql.asp)

onelinerhub: [How can I use variables in a MySQL query with Python?](https://onelinerhub.com/python-mysql/how-can-i-use-variables-in-a-mysql-query-with-python)