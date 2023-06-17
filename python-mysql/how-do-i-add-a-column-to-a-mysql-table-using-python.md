# How do I add a column to a MySQL table using Python?
// plain

To add a column to a MySQL table using Python, you need to use the ALTER TABLE statement. This statement is used to modify the structure of an existing table. For example:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"

mycursor.execute(sql)

print(mycursor.rowcount, "record(s) affected")
```

This will add a column named `id` to the `customers` table with an auto-incrementing integer as the primary key. The output will be `1 record(s) affected`.

## Code explanation


1. `import mysql.connector`: imports the MySQL Connector Python module.
2. `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword")`: connects to the MySQL database.
3. `mycursor = mydb.cursor()`: creates a cursor object.
4. `sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"`: the SQL statement to add a column to the `customers` table.
5. `mycursor.execute(sql)`: executes the SQL statement.
6. `print(mycursor.rowcount, "record(s) affected")`: prints the number of records affected.

## Helpful links

- [MySQL Connector Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL ALTER TABLE Statement Documentation](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html)

onelinerhub: [How do I add a column to a MySQL table using Python?](https://onelinerhub.com/python-mysql/how-do-i-add-a-column-to-a-mysql-table-using-python)