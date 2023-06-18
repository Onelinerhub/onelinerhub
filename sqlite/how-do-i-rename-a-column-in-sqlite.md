# How do I rename a column in SQLite?
// plain

To rename a column in SQLite, you use the `ALTER TABLE` command. The syntax for this command is `ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;`.

For example, if you wanted to rename the column `Name` to `FullName` in the `Employees` table, you would run the following command:

```sql
ALTER TABLE Employees RENAME COLUMN Name TO FullName;
```

This command does not return any output.

The parts of this command are:

- `ALTER TABLE`: This specifies that you are altering the table structure.
- `Employees`: This is the name of the table you are altering.
- `RENAME COLUMN`: This specifies that you are renaming a column.
- `Name`: This is the old column name.
- `TO`: This keyword indicates that you are changing the column name.
- `FullName`: This is the new column name.

## Helpful links

- [SQLite ALTER TABLE documentation](https://www.sqlite.org/lang_altertable.html)

onelinerhub: [How do I rename a column in SQLite?](https://onelinerhub.com/sqlite/how-do-i-rename-a-column-in-sqlite)