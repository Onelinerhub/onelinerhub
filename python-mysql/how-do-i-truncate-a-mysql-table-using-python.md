# How do I truncate a MySQL table using Python?
// plain

To truncate a MySQL table using Python, you can use the `TRUNCATE()` method of the `MySQLdb` library. This method is used to delete all rows from a table without deleting the table itself.

## Example code

```
import MySQLdb

db = MySQLdb.connect("localhost","user","password","database")

cursor = db.cursor()

cursor.execute("TRUNCATE TABLE table_name")

db.close()
```

The code above will delete all rows from the table `table_name` in the `database`.

## Code explanation


1. `import MySQLdb`: This imports the `MySQLdb` library, which is used to connect to and work with a MySQL database.

2. `db = MySQLdb.connect("localhost","user","password","database")`: This connects to the MySQL database with the given credentials (`user` and `password`) and selects the database `database`.

3. `cursor = db.cursor()`: This creates a cursor object which is used to execute queries.

4. `cursor.execute("TRUNCATE TABLE table_name")`: This executes the `TRUNCATE()` method which deletes all rows from the table `table_name`.

5. `db.close()`: This closes the connection to the database.

## Helpful links

- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/user_guide.html)
- [MySQL TRUNCATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/truncate-table.html)

onelinerhub: [How do I truncate a MySQL table using Python?](https://onelinerhub.com/python-mysql/how-do-i-truncate-a-mysql-table-using-python)