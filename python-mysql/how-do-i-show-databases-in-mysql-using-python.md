# How do I show databases in MySQL using Python?
// plain

To show databases in MySQL using Python, you can use the `show databases` command in the `MySQLdb` package. This package is a Python interface for interacting with a MySQL server. To use this command, you must first establish a connection to the MySQL server.

```python
import MySQLdb as mdb

con = mdb.connect('localhost', 'user', 'password', 'database')

cur = con.cursor()

cur.execute("show databases")

for x in cur:
  print(x)
```

The above code will output a list of all the databases in the MySQL server:

```
('information_schema',)
('mysql',)
('mydb',)
('performance_schema',)
('sys',)
```

The code is composed of the following parts:

1. `import MySQLdb as mdb`: This imports the `MySQLdb` package and assigns it to the variable `mdb`.
2. `con = mdb.connect('localhost', 'user', 'password', 'database')`: This establishes a connection to the MySQL server.
3. `cur = con.cursor()`: This creates a cursor object which will be used to execute commands.
4. `cur.execute("show databases")`: This executes the `show databases` command which retrieves a list of databases from the MySQL server.
5. `for x in cur:`: This iterates through the list of databases returned from the `show databases` command.
6. `print(x)`: This prints each database in the list of databases.

For more information, see the following links:

- [MySQLdb package documentation](https://mysqlclient.readthedocs.io/user_guide.html)
- [MySQL SHOW DATABASES command](https://dev.mysql.com/doc/refman/8.0/en/show-databases.html)

onelinerhub: [How do I show databases in MySQL using Python?](https://onelinerhub.com/python-mysql/how-do-i-show-databases-in-mysql-using-python)