# How can I get the column names from a MySQL database using Python?
// plain

You can get the column names from a MySQL database using Python by using the `cursor.description` attribute. This attribute returns information about the columns in the result set of a query as a sequence of `7-item tuples`. Here is an example:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

for x in mycursor.description:
  print(x[0])

# Output:
# name
# address
# age
```

The code above connects to a MySQL database, executes a query and prints the column names from the result set. The `mycursor.description` attribute returns a sequence of 7-item tuples. Each tuple contains information about the columns in the result set, with the first item in the tuple being the column name.

## Helpful links
* [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)
* [MySQL Connector/Python Cursor Objects](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html)

onelinerhub: [How can I get the column names from a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-get-the-column-names-from-a-mysql-database-using-python)