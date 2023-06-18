# How do I use SQLite REPLACE to update existing records in a database?
// plain

SQLite REPLACE is used to update existing records in a database. It is similar to the SQL UPDATE command, but with REPLACE, you can update a record if it already exists, or insert a new record if it does not exist.

The syntax for REPLACE is as follows:

```
REPLACE INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

For example, if we wanted to update the name of an existing record in a table called "customers", we could use the following command:

```
REPLACE INTO customers (id, name)
VALUES (1, 'John Doe');
```

This command would update the name of the customer with an ID of 1 to "John Doe". If there was no record with an ID of 1, then a new record would be inserted.

The parts of the REPLACE command are:

- REPLACE INTO: This is the keyword for the command.
- table_name: This is the name of the table to be modified.
- column1, column2, ...: This is a list of the columns to be modified.
- VALUES: This is the keyword that indicates the values to be inserted or updated.
- value1, value2, ...: This is a list of values to be inserted or updated.

For more information on SQLite REPLACE, see the following links:
- [SQLite Documentation](https://sqlite.org/lang_replace.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-replace/)

onelinerhub: [How do I use SQLite REPLACE to update existing records in a database?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-replace-to-update-existing-records-in-a-database)