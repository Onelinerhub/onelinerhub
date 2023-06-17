# How do I use Python to fetch all records from a MySQL database?
// plain

To use Python to fetch all records from a MySQL database, you need to:
1. Install the MySQL Connector/Python library: `pip install mysql-connector-python`
2. Create a connection to the MySQL database:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)
```
3. Create a cursor object to traverse the records:
```
mycursor = mydb.cursor()
```
4. Execute an SQL query to fetch the records:
```
mycursor.execute("SELECT * FROM your_table")
```
5. Fetch all the records from the cursor object:
```
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```
6. Output:
```
('John', 'Highway 21')
('Amy', 'Mountain 21')
('Hannah', 'Valley 345')
```

## Helpful links
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Tutorial](https://pynative.com/python-mysql-tutorial/)

onelinerhub: [How do I use Python to fetch all records from a MySQL database?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-fetch-all-records-from-a-mysql-database)