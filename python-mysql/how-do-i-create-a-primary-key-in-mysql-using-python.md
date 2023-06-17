# How do I create a primary key in MySQL using Python?
// plain

Creating a primary key in MySQL using Python is a simple process. The following example code will create a table called ‘students’ with a primary key called ‘id’:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

```

This code will create a table called ‘students’ with a primary key called ‘id’. The ‘id’ column is set to auto-increment, which means it will automatically increment each time a new record is inserted.

The code consists of the following parts:
- `import mysql.connector`: This imports the mysql.connector library which is used to connect to the MySQL database.
- `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword", database="mydatabase")`: This establishes a connection to the MySQL database.
- `mycursor = mydb.cursor()`: This creates a cursor object which is used to execute queries.
- `mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")`: This creates a table called ‘students’ with a primary key called ‘id’, and two additional columns called ‘name’ and ‘address’.

No output will be displayed when the code is run.

## Helpful links
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)

onelinerhub: [How do I create a primary key in MySQL using Python?](https://onelinerhub.com/python-mysql/how-do-i-create-a-primary-key-in-mysql-using-python)