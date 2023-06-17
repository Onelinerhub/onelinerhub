# How do I connect to XAMPP MySQL using Python?
// plain

To connect to XAMPP MySQL using Python, you need to use the `mysql.connector` library.

A basic example of connecting to a local MySQL database with `mysql.connector` would be:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
```

The output of the above code would be something like:

```
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f8f2b7f8e10>
```

The code consists of the following parts:

1. Import the `mysql.connector` library.
2. Create a `mydb` variable with the `mysql.connector.connect` method, passing in the host, user and passwd arguments.
3. Print the `mydb` variable.

## Helpful links

- [mysql.connector Documentation](https://dev.mysql.com/doc/connector-python/en/)

onelinerhub: [How do I connect to XAMPP MySQL using Python?](https://onelinerhub.com/python-mysql/how-do-i-connect-to-xampp-mysql-using-python)