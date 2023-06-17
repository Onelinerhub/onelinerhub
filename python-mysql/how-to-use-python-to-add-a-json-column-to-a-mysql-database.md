# How to use Python to add a JSON column to a MySQL database?
// plain

To add a JSON column to a MySQL database using Python, the following steps should be taken:

1. Establish a connection to the MySQL database using the `mysql.connector` library.

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="password",
  database="mydatabase"
)
```

2. Create a JSON column in the database using the `ALTER TABLE` command.

```sql
ALTER TABLE mytable ADD json_column JSON;
```

3. Insert the JSON data into the column using the `INSERT INTO` command.

```python
mycursor = mydb.cursor()

sql = "INSERT INTO mytable (json_column) VALUES (%s)"
val = ('{"name":"John","age":30,"city":"New York"}',)

mycursor.execute(sql, val)
mydb.commit()
```

4. Check that the data was successfully inserted by querying the table.

```sql
SELECT * FROM mytable;
```

## Output example

```
+----+------------------------------------+
| id | json_column                        |
+----+------------------------------------+
|  1 | {"name":"John","age":30,"city":"NY"}|
+----+------------------------------------+
```

## Helpful links
- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL ALTER TABLE Syntax](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html)
- [MySQL INSERT INTO Syntax](https://dev.mysql.com/doc/refman/8.0/en/insert.html)

onelinerhub: [How to use Python to add a JSON column to a MySQL database?](https://onelinerhub.com/python-mysql/how-to-use-python-to-add-a-json-column-to-a-mysql-database)