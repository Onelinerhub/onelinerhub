# How do I install the Python MySQL Connector?
// plain

1. Installing the Python MySQL Connector is easy with the help of the pip package manager.
2. Open a terminal window and type the following command: `pip install mysql-connector-python`
3. This will install the connector and all of its dependencies.
4. To test the installation, try connecting to a MySQL database with the following code:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
```

## Output example

```
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f7fb7f2c7f0>
```

5. The above code connects to a MySQL database using the credentials provided and returns a connection object.
6. If you get an error, check out the [documentation](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html) for more information on how to set up the connection.
7. You can also find more examples of how to use the connector [here](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html).

onelinerhub: [How do I install the Python MySQL Connector?](https://onelinerhub.com/python-mysql/how-do-i-install-the-python-mysql-connector)