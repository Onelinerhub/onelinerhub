# How can I connect to a MySQL database using Python?
// plain

1. Install the MySQL Connector/Python package:
   ```pip install mysql-connector-python```

2. Establish a connection to the MySQL database by creating a new ```MySQLConnection``` object:
   ```
   import mysql.connector
   mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      passwd="yourpassword"
   )
   ```

3. Create a new ```MySQLCursor``` object from the connection:
   ```
   mycursor = mydb.cursor()
   ```

4. Use the ```execute()``` method of the cursor object to execute a MySQL query:
   ```
   mycursor.execute("SELECT * FROM customers")
   ```

5. Fetch all the rows from the cursor object using the ```fetchall()``` method:
   ```
   myresult = mycursor.fetchall()
   for x in myresult:
     print(x)
   ```
   Output:
   ```
   (1, 'John', 'Highway 21')
   (2, 'Peter', 'Lowstreet 4')
   (3, 'Amy', 'Apple st 652')
   (4, 'Hannah', 'Mountain 21')
   ```

6. Close the cursor and connection objects, once your work is finished:
   ```
   mycursor.close()
   mydb.close()
   ```

7. For more information on connecting to a MySQL database using Python, please refer to the official [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I connect to a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-connect-to-a-mysql-database-using-python-1686988119)