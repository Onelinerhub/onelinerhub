# How do I connect to a MySQL database using Python?
// plain

To connect to a MySQL database using Python, you need to use a MySQL Connector. MySQL Connector/Python is a standardized database driver for Python platforms and development.

To connect to a MySQL database with Python, you need to use the following steps:

1. Install MySQL Connector Python using the pip command: ```pip install mysql-connector-python```
2. Import the MySQL Connector Python module in your program: ```import mysql.connector```
3. Establish a connection to the MySQL database by creating a new MySQLConnection object: ```mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")```
4. Create a new cursor object from the connection: ```mycursor = mydb.cursor()```
5. Execute a SQL query: ```mycursor.execute("SELECT * FROM customers")```
6. Fetch the results: ```myresult = mycursor.fetchall()```
7. Print the results: ```for x in myresult: print(x)```

The output of the above code is a list of records from the customers table:

```
('John', 'Highway 21')
('Peter', 'Lowstreet 4')
('Amy', 'Apple st 652')
('Hannah', 'Mountain 21')
('Michael', 'Valley 345')
('Sandy', 'Ocean blvd 2')
('Betty', 'Green Grass 1')
('Richard', 'Sky st 331')
('Susan', 'One way 98')
('Vicky', 'Yellow Garden 2')
('Ben', 'Park Lane 38')
('William', 'Central st 954')
('Chuck', 'Main Road 989')
('Viola', 'Sideway 1633')
```

## Helpful links
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [Python MySQL Tutorial](https://pynative.com/python-mysql-tutorial/)

onelinerhub: [How do I connect to a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-connect-to-a-mysql-database-using-python)