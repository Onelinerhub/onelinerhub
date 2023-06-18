# How can I resolve the error "no such table" when using SQLite?
// plain

When using SQLite, the error "no such table" can be resolved by creating the table in the database. To do this, the user must first connect to the database. This can be done with the following code:

```
import sqlite3

conn = sqlite3.connect('database.db')
```

Once connected, the user can create the table with the following code:

```
conn.execute('''CREATE TABLE table_name
    (column_1 datatype, column_2 datatype, ...);''')
```

In this code:

* `CREATE TABLE` is the command used to create a table.
* `table_name` is the name of the table being created.
* `column_1` and `column_2` are the names of the columns being created in the table.
* `datatype` is the type of data that will be stored in the column (e.g. integer, text, date).

Once the table has been created, the user can then insert data into the table.

```
conn.execute("INSERT INTO table_name VALUES (value_1, value_2, ...);")
```

In this code:

* `INSERT INTO` is the command used to insert data into the table.
* `table_name` is the name of the table the data is being inserted into.
* `value_1` and `value_2` are the values being inserted into the table.

Once the table has been created and the data has been inserted, the user can then query the table.

```
cursor = conn.execute("SELECT * FROM table_name;")
for row in cursor:
    print(row)
```

In this code:

* `SELECT` is the command used to query the table.
* `table_name` is the name of the table being queried.
* `cursor` is an object used to iterate over the rows in the query result.
* `row` is an object containing the data from each row in the query result.

The output of this code will be the data from the table:

```
('value_1', 'value_2', ...)
('value_1', 'value_2', ...)
...
```

## Helpful links

* [SQLite Tutorial](https://www.sqlitetutorial.net/)
* [SQLite CREATE TABLE](https://www.sqlitetutorial.net/sqlite-create-table/)
* [SQLite INSERT](https://www.sqlitetutorial.net/sqlite-insert/)
* [SQLite SELECT](https://www.sqlitetutorial.net/sqlite-select/)

onelinerhub: [How can I resolve the error "no such table" when using SQLite?](https://onelinerhub.com/sqlite/how-can-i-resolve-the-error--no-such-table--when-using-sqlite)