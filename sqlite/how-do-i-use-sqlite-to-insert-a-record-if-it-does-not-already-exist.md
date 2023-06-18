# How do I use SQLite to insert a record if it does not already exist?
// plain

The following example code can be used to insert a record into a SQLite table if it does not already exist:

```
INSERT OR IGNORE INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

This statement will attempt to insert the specified values into the specified columns of the table. If the record already exists, the statement will be ignored.

The code consists of the following parts:
- `INSERT OR IGNORE`: This is the keyword that tells SQLite to insert the record if it does not already exist
- `INTO table_name`: This specifies the name of the table to insert the record into
- `(column1, column2, column3)`: This specifies the columns of the table to insert the values into
- `VALUES (value1, value2, value3)`: This specifies the values to be inserted into the columns

## Helpful links
- [SQLite Insert](https://www.sqlitetutorial.net/sqlite-insert/)
- [SQLite INSERT OR IGNORE](https://www.sqlitetutorial.net/sqlite-insert-or-ignore/)

onelinerhub: [How do I use SQLite to insert a record if it does not already exist?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-to-insert-a-record-if-it-does-not-already-exist)