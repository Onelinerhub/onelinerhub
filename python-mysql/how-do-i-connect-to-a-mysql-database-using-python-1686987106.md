# How do I connect to a MySQL database using Python?
// plain

To connect to a MySQL database using Python, the following steps need to be taken:

1.  Install the MySQL Connector/Python package. This can be done using `pip install mysql-connector-python` or `conda install -c anaconda mysql-connector-python` depending on the environment.

2. Create a connection object using the `connect()` method. This requires the hostname, username, password, and database name. For example:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

print(mydb)

# Output: <mysql.connector.connection.MySQLConnection object at 0x7f3c8d7a7a00>
```

3. Create a cursor object using the `cursor()` method. This will allow us to execute SQL statements. For example:

```python
mycursor = mydb.cursor()
```

4. Execute an SQL statement using the `execute()` method. For example:

```python
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Output:
# ('John', 'Highway 21')
# ('Peter', 'Lowstreet 4')
# ('Amy', 'Apple st 652')
# ('Hannah', 'Mountain 21')
```

5. Close the connection using the `close()` method. For example:

```python
mydb.close()
```

## Helpful links

- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Tutorial](https://www.w3schools.com/sql/default.asp)

onelinerhub: [How do I connect to a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-connect-to-a-mysql-database-using-python-1686987106)