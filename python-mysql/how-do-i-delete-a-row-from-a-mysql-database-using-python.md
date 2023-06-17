# How do I delete a row from a MySQL database using Python?
// plain

To delete a row from a MySQL database using Python, you can use the `cursor.execute()` method of the `MySQLConnection` object. This method takes two parameters: the query string and a list of parameters to be used in the query.

The query string should be a `DELETE` statement, followed by the `WHERE` clause containing the conditions for which rows should be deleted.

Below is an example of deleting a row from a table named `students`:

```python
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(user='user', password='password',
                              host='localhost',
                              database='school')

# Create a cursor object
cursor = conn.cursor()

# Execute the query
cursor.execute("DELETE FROM students WHERE name = %s", ('John',))

# Commit the changes
conn.commit()
```

## Code explanation


1. `import mysql.connector`: This imports the MySQL Connector/Python library.
2. `conn = mysql.connector.connect(user='user', password='password', host='localhost', database='school')`: This creates a connection object to the MySQL database.
3. `cursor = conn.cursor()`: This creates a cursor object to execute the query.
4. `cursor.execute("DELETE FROM students WHERE name = %s", ('John',))`: This executes the `DELETE` statement with the parameter `'John'` to delete the row from the `students` table where the `name` column is equal to `'John'`.
5. `conn.commit()`: This commits the changes to the database.

## Helpful links

- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL DELETE Statement](https://dev.mysql.com/doc/refman/8.0/en/delete.html)

onelinerhub: [How do I delete a row from a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-delete-a-row-from-a-mysql-database-using-python)