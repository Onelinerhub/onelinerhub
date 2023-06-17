# How can I check the version of MySQL I'm using with Python?
// plain

You can check the version of MySQL you are using with Python by using the `mysql-connector-python` library.

Below is an example code block to check the version:
```
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

# Print the version of MySQL
print(mydb.get_server_info())
```

The output of this code block would be something like `8.0.20`.

The code can be broken down into the following parts:

1. `import mysql.connector` - This imports the `mysql-connector-python` library, which allows us to connect to the MySQL database and perform queries.

2. `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")` - This creates a connection to the MySQL database using the credentials provided.

3. `print(mydb.get_server_info())` - This prints the version of MySQL that is being used.

For more information, please refer to the [MySQL Connector/Python documentation](https://dev.mysql.com/doc/connector-python/en/).

onelinerhub: [How can I check the version of MySQL I'm using with Python?](https://onelinerhub.com/python-mysql/how-can-i-check-the-version-of-mysql-i-m-using-with-python)