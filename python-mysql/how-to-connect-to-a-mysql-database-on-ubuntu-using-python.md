# How to connect to a MySQL database on Ubuntu using Python?
// plain

To connect to a MySQL database on Ubuntu using Python, we need to install the `mysql-connector-python` package. This can be done by running the following command in the terminal:

```
sudo apt-get install mysql-connector-python
```

Once the package is installed, we can use the `mysql.connector` module to connect to the MySQL database. For example, the following code will connect to the `mydb` database using the `root` user and `password` as the password:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mydb"
)

print(mydb)
```

The output of the code will be an object representing the connection to the MySQL database.

The code consists of the following parts:

1. `import mysql.connector`: This imports the `mysql.connector` module, which provides the necessary functions for connecting to the MySQL database.
2. `mydb = mysql.connector.connect()`: This creates a connection object, which is stored in the `mydb` variable. The `connect()` function takes the following arguments:
    * `host`: The hostname or IP address of the MySQL server.
    * `user`: The username of the MySQL user.
    * `passwd`: The password of the MySQL user.
    * `database`: The name of the MySQL database.
3. `print(mydb)`: This prints out the connection object, which confirms that the connection to the MySQL database was successful.

For more information, please refer to the following links:

* [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
* [Connecting to MySQL Using Connector/Python](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)

onelinerhub: [How to connect to a MySQL database on Ubuntu using Python?](https://onelinerhub.com/python-mysql/how-to-connect-to-a-mysql-database-on-ubuntu-using-python)