# How do I rename a column in PostgreSQL?
// plain

Renaming a column in PostgreSQL is a simple process and can be done using the `ALTER TABLE` command.

## Example code

```
ALTER TABLE table_name
RENAME COLUMN old_column_name TO new_column_name;
```

The code above will rename the column `old_column_name` to `new_column_name` in the `table_name` table.

## Code explanation

1. `ALTER TABLE` - This command is used to modify the structure of an existing table.
2. `table_name` - This is the name of the table which contains the column to be renamed.
3. `RENAME COLUMN` - This command is used to rename an existing column.
4. `old_column_name` - This is the name of the column to be renamed.
5. `TO` - This keyword is used to separate the old and new column names.
6. `new_column_name` - This is the new name of the column.

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/9.5/sql-altertable.html)
- [Stack Overflow](https://stackoverflow.com/questions/13842468/how-to-rename-a-column-in-postgresql)

onelinerhub: [How do I rename a column in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-rename-a-column-in-postgresql)