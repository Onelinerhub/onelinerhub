# How do Python and MySQL compare to MariaDB?
// plain

Python and MySQL can be used together to create powerful applications that can store and retrieve data from a MySQL database. However, MariaDB is a newer, more advanced open source database that provides a more robust feature set than MySQL.

MariaDB supports improved performance, scalability, and security compared to MySQL. For example, MariaDB supports advanced features such as row-level locking, which allows multiple transactions to be processed simultaneously.

MariaDB also supports a wide range of storage engines, such as XtraDB, which provides improved performance and scalability compared to MySQL’s MyISAM engine.

Python can be used to connect to MariaDB using a variety of database drivers, such as PyMySQL, which provides an interface compatible with MySQL.

## Example code

```
import pymysql

# Connect to the database
conn = pymysql.connect(host="localhost", user="root", password="password", db="testdb")

# Execute a query
cur = conn.cursor()
cur.execute("SELECT * FROM users")

# Print the results
for row in cur:
    print(row)

# Close the connection
conn.close()
```

## Output example

```
('John', 'Smith', 'john@example.com')
('Jane', 'Doe', 'jane@example.com')
```

- `import pymysql`: imports the PyMySQL library, which provides an interface compatible with MySQL.
- `conn = pymysql.connect(host="localhost", user="root", password="password", db="testdb")`: creates a connection to the MariaDB database.
- `cur = conn.cursor()`: creates a cursor object, which is used to execute queries.
- `cur.execute("SELECT * FROM users")`: executes a query to select all records from the users table.
- `for row in cur:`: iterates over the results of the query and prints them.
- `conn.close()`: closes the connection to the database.

## Helpful links
- [PyMySQL Documentation](https://pymysql.readthedocs.io/en/latest/)
- [MariaDB Documentation](https://mariadb.com/kb/en/library/documentation/)

onelinerhub: [How do Python and MySQL compare to MariaDB?](https://onelinerhub.com/python-mysql/how-do-python-and-mysql-compare-to-mariadb)