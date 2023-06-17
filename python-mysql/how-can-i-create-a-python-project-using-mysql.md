# How can I create a Python project using MySQL?
// plain

Creating a Python project using MySQL is fairly straightforward. First, you will need to install the MySQL Connector Python library. This library will allow you to connect to a MySQL database and execute queries.

Once the library is installed, you can create a connection to the MySQL database. The following example code creates a connection to a MySQL database called `my_database`:
```
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="my_database"
)
```

Once the connection is established, you can execute queries on the database using the `execute()` method. For example, the following code will create a table called `my_table`:
```
cursor = db.cursor()
cursor.execute("CREATE TABLE my_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
```

After the table is created, you can use the `INSERT` statement to add data to the table. The following code adds a row to the `my_table` table:
```
cursor.execute("INSERT INTO my_table (name) VALUES ('John')")
```

Finally, you can use the `SELECT` statement to retrieve data from the table. The following code retrieves all rows from the `my_table` table:
```
cursor.execute("SELECT * FROM my_table")

for row in cursor.fetchall():
  print(row)
```
## Output example

```
(1, 'John')
```

For more information on creating a Python project using MySQL, see the [MySQL Connector Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I create a Python project using MySQL?](https://onelinerhub.com/python-mysql/how-can-i-create-a-python-project-using-mysql)