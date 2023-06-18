# How do I truncate a table in SQLite?
// plain

Truncating a table in SQLite is a fairly straightforward process. To do so, you can use the `DELETE` statement. The syntax for this statement is as follows:

```
DELETE FROM <table_name>;
```

This statement will delete all the rows from the specified table. To delete all the data from the table while preserving the table structure, you can use the `DROP TABLE` statement. The syntax for this is as follows:

```
DROP TABLE <table_name>;
```

This statement will delete the entire table, including its structure and data. After executing either of these statements, the table will be empty.

Here is an example of truncating a table called `users`:

```
DELETE FROM users;
```

No output is generated.

#### List of code parts

1. `DELETE FROM` - the keyword to delete all rows from a table
2. `<table_name>` - the name of the table to truncate
3. `DROP TABLE` - the keyword to delete the entire table, including its structure and data
4. `<table_name>` - the name of the table to drop

#### Relevant Links

1. [SQLite DELETE Statement](https://www.sqlitetutorial.net/sqlite-delete/)
2. [SQLite DROP TABLE Statement](https://www.sqlitetutorial.net/sqlite-drop-table/)

onelinerhub: [How do I truncate a table in SQLite?](https://onelinerhub.com/sqlite/how-do-i-truncate-a-table-in-sqlite)