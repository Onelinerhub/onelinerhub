# How do I use the Python MySQL library?
// plain

The Python MySQL library is a library that provides access to the MySQL database from Python. It allows you to connect to a MySQL server, execute queries, and retrieve results.

To use the library, first you need to install the library with `pip install mysql-connector-python`.

Then create a connection to the MySQL server:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd"
)
```

Once the connection is established, you can execute queries on the database:
```
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

The output of the code above would be a list of all the records in the `customers` table:
```
(1, 'John', 'Highway 21')
(2, 'Peter', 'Lowstreet 4')
(3, 'Amy', 'Apple st 652')
(4, 'Hannah', 'Mountain 21')
```

The Python MySQL library also provides methods to insert, update, and delete records from the database.

For more information on using the Python MySQL library, please refer to the following links:
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Tutorial](https://pynative.com/python-mysql-tutorial/)

onelinerhub: [How do I use the Python MySQL library?](https://onelinerhub.com/python-mysql/how-do-i-use-the-python-mysql-library)