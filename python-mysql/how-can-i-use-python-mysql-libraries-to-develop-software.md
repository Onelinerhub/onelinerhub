# How can I use Python MySQL libraries to develop software?
// plain

Python can be used to develop software that interacts with a MySQL database. To do this, you need to use one of the Python MySQL libraries. Examples of such libraries are `mysql-connector`, `MySQLdb`, and `PyMySQL`.

Below is an example using the `mysql-connector` library:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

```

## Output example


```
('information_schema',)
('mydatabase',)
('mysql',)
('performance_schema',)
('sys',)
```

The code above:
1. Imports the `mysql.connector` library
2. Connects to the database
3. Creates a cursor
4. Executes a SQL query
5. Iterates over the result set and prints each row

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Tutorial](https://www.w3schools.com/python/python_mysql_getstarted.asp)

onelinerhub: [How can I use Python MySQL libraries to develop software?](https://onelinerhub.com/python-mysql/how-can-i-use-python-mysql-libraries-to-develop-software)