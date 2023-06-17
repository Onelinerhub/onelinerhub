# How do I rename a table in PostgreSQL?
// plain

Renaming a table in PostgreSQL is done using the `ALTER TABLE` command. This command allows you to change the name of the table as well as other properties. Here is an example of how to rename a table:

```
ALTER TABLE old_table_name RENAME TO new_table_name;
```

This command will rename the table `old_table_name` to `new_table_name`.

The command consists of the following parts:

- `ALTER TABLE` - This is the command to alter the table.
- `old_table_name` - This is the name of the table to be renamed.
- `RENAME TO` - This clause indicates that the table is to be renamed.
- `new_table_name` - This is the new name of the table.

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-altertable.html).

onelinerhub: [How do I rename a table in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-rename-a-table-in-postgresql)