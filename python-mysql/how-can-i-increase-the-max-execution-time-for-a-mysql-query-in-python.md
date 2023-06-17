# How can I increase the max_execution_time for a MySQL query in Python?
// plain

The max_execution_time for a MySQL query in Python can be increased by setting the `connect_timeout` option in the connection string. This option sets the maximum amount of time (in seconds) that the server will wait for a connection to be established before timing out.

## Example code

```
import mysql.connector

cnx = mysql.connector.connect(user='user', password='password',
                              host='127.0.0.1',
                              database='mydb',
                              connect_timeout=60)
```

The `connect_timeout` option can be set to any value, depending on the amount of time needed for the query to complete.

## Code explanation

1. `import mysql.connector`: imports the MySQL Connector/Python library, which is needed to establish a connection to a MySQL database.
2. `cnx = mysql.connector.connect(user='user', password='password', host='127.0.0.1', database='mydb', connect_timeout=60)`: establishes a connection to the MySQL database using the specified user, password, host, and database. The `connect_timeout` option is set to 60 seconds, which is the maximum amount of time the server will wait for a connection to be established before timing out.
3. `connect_timeout`: sets the maximum amount of time (in seconds) that the server will wait for a connection to be established before timing out.

## Helpful links
- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Connector/Python Connection Arguments](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html)

onelinerhub: [How can I increase the max_execution_time for a MySQL query in Python?](https://onelinerhub.com/python-mysql/how-can-i-increase-the-max-execution-time-for-a-mysql-query-in-python)