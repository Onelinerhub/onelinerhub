# How do I delete a column in an SQLite database?
// plain

To delete a column in an SQLite database, you can use the `ALTER TABLE` statement. The syntax is as follows:

```
ALTER TABLE table_name DROP COLUMN column_name;
```

For example, if you have a table called `students` and want to delete the `age` column, you can execute the following statement:

```
ALTER TABLE students DROP COLUMN age;
```

This statement will drop the `age` column from the `students` table.

The parts of this statement are:
- `ALTER TABLE`: This statement is used to modify the structure of an existing table.
- `table_name`: This is the name of the table you want to modify.
- `DROP COLUMN`: This clause is used to delete a column from the table.
- `column_name`: This is the name of the column you want to delete.

Here are some ## Helpful links
- [SQLite ALTER TABLE documentation](https://www.sqlite.org/lang_altertable.html)
- [SQLite DROP COLUMN documentation](https://www.sqlite.org/lang_altertable.html#droppedcolumn)

onelinerhub: [How do I delete a column in an SQLite database?](https://onelinerhub.com/sqlite/how-do-i-delete-a-column-in-an-sqlite-database)