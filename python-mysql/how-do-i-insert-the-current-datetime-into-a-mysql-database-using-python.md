# How do I insert the current datetime into a MySQL database using Python?
// plain

Using Python, you can insert the current datetime into a MySQL database by first creating a `datetime` object and then using the `cursor.execute()` method. The following example code block shows how to do this:

```
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address, date_time) VALUES (%s, %s, %s)"
val = ("John", "Highway 21", datetime.now())

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

## Output example

```
1 record inserted.
```

The code can be broken down into the following parts:

1. Import the `mysql.connector` and `datetime` modules.
2. Connect to the MySQL database.
3. Create a `datetime` object.
4. Create an SQL query with placeholders for the values.
5. Execute the query with the `datetime` object as one of the values.
6. Commit the changes to the database.
7. Print the number of records inserted.

## Helpful links

- [Python MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
- [Python datetime module](https://docs.python.org/3/library/datetime.html)

onelinerhub: [How do I insert the current datetime into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-insert-the-current-datetime-into-a-mysql-database-using-python)