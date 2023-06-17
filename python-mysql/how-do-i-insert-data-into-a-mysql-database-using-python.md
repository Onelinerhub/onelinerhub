# How do I insert data into a MySQL database using Python?
// plain

To insert data into a MySQL database using Python, use the PyMySQL library.

## Example code

```
import pymysql

# Open database connection
db = pymysql.connect("localhost","user","password","database" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
   ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
```

This code will insert a record into the EMPLOYEE table in the database. The record will contain the values 'Mac', 'Mohan', 20, 'M', and 2000 for the columns FIRST_NAME, LAST_NAME, AGE, SEX, and INCOME respectively.

## Code explanation

- `import pymysql`: imports the PyMySQL library
- `db = pymysql.connect("localhost","user","password","database" )`: opens a connection to the MySQL database
- `cursor = db.cursor()`: creates a cursor object to execute queries
- `sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
   ('Mac', 'Mohan', 20, 'M', 2000)`: prepares the SQL query to insert a record into the EMPLOYEE table
- `cursor.execute(sql)`: executes the prepared SQL query
- `db.commit()`: commits the changes to the database
- `db.rollback()`: rolls back the changes in case of an error
- `db.close()`: closes the connection to the database

## Helpful links
- [PyMySQL Documentation](https://pymysql.readthedocs.io/en/latest/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

onelinerhub: [How do I insert data into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-insert-data-into-a-mysql-database-using-python)