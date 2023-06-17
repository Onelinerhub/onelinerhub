# How do I truncate a table in PostgreSQL?
// plain

To truncate a table in PostgreSQL, you can use the `TRUNCATE` command. This command removes all rows from the table quickly and efficiently.

## Example code

```
TRUNCATE TABLE my_table;
```

The code above will remove all rows from the table `my_table`. No output will be returned.

The `TRUNCATE` command has the following parts:
- `TRUNCATE` - the command to truncate a table
- `TABLE` - specifies that you are truncating a table
- `my_table` - the name of the table you are truncating

For more information, please see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-truncate.html).

onelinerhub: [How do I truncate a table in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-truncate-a-table-in-postgresql)