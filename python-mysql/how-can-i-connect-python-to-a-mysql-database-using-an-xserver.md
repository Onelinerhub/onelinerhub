# How can I connect Python to a MySQL database using an Xserver?
// plain

To connect Python to a MySQL database using an Xserver you must have the following prerequisites installed:

1. Python 3.7+
2. MySQL Server
3. Xserver

Once the prerequisites are installed, the following steps must be taken to connect Python to the MySQL database using an Xserver:

1. Import the necessary packages:
```
import mysql.connector
import xserver
```

2. Create a connection object:
```
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password"
)
```

3. Create a cursor object:
```
mycursor = mydb.cursor()
```

4. Execute an SQL query:
```
mycursor.execute("SELECT * FROM customers")
```

5. Fetch the results:
```
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

6. Output (if any):
```
('John', 'Highway 21')
('Peter', 'Lowstreet 4')
('Amy', 'Apple st 652')
('Hannah', 'Mountain 21')
```

7. Close the connection:
```
mydb.close()
```

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [Xserver Documentation](https://www.x.org/wiki/Documentation/)

onelinerhub: [How can I connect Python to a MySQL database using an Xserver?](https://onelinerhub.com/python-mysql/how-can-i-connect-python-to-a-mysql-database-using-an-xserver)