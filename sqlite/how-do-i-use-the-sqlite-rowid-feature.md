# How do I use the SQLite rowid feature?
// plain

SQLite rowid is a special column in every row of a table that can be used to uniquely identify a row. It is a 64-bit signed integer that is automatically generated when a new row is inserted into the table.

The rowid can be used in SELECT, UPDATE, and DELETE statements to identify a row. For example:

```
SELECT * FROM table WHERE rowid = 5;
```

This statement will return the row with rowid equal to 5.

The rowid can also be used in UPDATE and DELETE statements. For example:

```
DELETE FROM table WHERE rowid = 5;
```

This statement will delete the row with rowid equal to 5.

The rowid feature can also be used to return the rowid of a row. For example:

```
SELECT rowid FROM table WHERE id = 5;
```

This statement will return the rowid of the row with id equal to 5.

It is important to note that the rowid is not guaranteed to be stable. It can change if rows are added, deleted, or updated in the table.

## Helpful links
- [SQLite Documentation on Rowid](https://www.sqlite.org/rowidtable.html)
- [SQLite Tutorial](https://www.tutorialspoint.com/sqlite/sqlite_row_id.htm)

onelinerhub: [How do I use the SQLite rowid feature?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-rowid-feature)