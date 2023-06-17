# How do I insert a date into a MySQL database using Python?
// plain

To insert a date into a MySQL database using Python, the following steps can be followed:
1. Import the necessary packages:
   ```
   import mysql.connector
   from datetime import datetime
   ```
2. Establish a connection to the MySQL database:
   ```
   mydb = mysql.connector.connect(
     host="localhost",
     user="user",
     passwd="passwd",
     database="mydatabase"
   )
   ```
3. Create a cursor object and use it to execute a query:
   ```
   mycursor = mydb.cursor()
   sql = "INSERT INTO customers (name, address, date_of_birth) VALUES (%s, %s, %s)"
   ```
4. Create a date object in the desired format:
   ```
   date_of_birth = datetime.strptime('1995-10-12', '%Y-%m-%d').date()
   ```
5. Pass the date object as a parameter to the query:
   ```
   val = ("John", "Highway 21", date_of_birth)
   mycursor.execute(sql, val)
   ```
6. Commit the changes to the database:
   ```
   mydb.commit()
   ```
7. Print a success message:
   ```
   print(mycursor.rowcount, "record inserted.")
   ```
   Output: 1 record inserted.

## Code explanation
**
- Import the necessary packages: This imports the `mysql.connector` package, which is used to connect to the MySQL database, and the `datetime` package, which is used to create a date object in the desired format.
- Establish a connection to the MySQL database: This creates a connection to the MySQL database using the given credentials.
- Create a cursor object and use it to execute a query: This creates a cursor object, which is used to execute SQL queries, and a query that inserts a date into the database.
- Create a date object in the desired format: This creates a date object in the desired format using the `datetime.strptime()` method.
- Pass the date object as a parameter to the query: This passes the date object as a parameter to the query.
- Commit the changes to the database: This commits the changes to the database.
- Print a success message: This prints a success message after the changes have been committed.

**## Helpful links**
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [Python datetime Module](https://docs.python.org/3/library/datetime.html)

onelinerhub: [How do I insert a date into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-insert-a-date-into-a-mysql-database-using-python)