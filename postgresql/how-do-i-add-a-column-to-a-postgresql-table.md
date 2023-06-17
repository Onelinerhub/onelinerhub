# How do I add a column to a PostgreSQL table?
// plain

Adding a column to a PostgreSQL table is a common database operation. To do this, you will need to use the `ALTER TABLE` command. Here is an example of how to add a new column to a table:

```
ALTER TABLE table_name
ADD COLUMN column_name data_type;
```

This command will add a new column named `column_name` to the `table_name` table with the data type `data_type`. For example, if you wanted to add a column named `age` to the `users` table with the data type `integer`, you would use the following command:

```
ALTER TABLE users
ADD COLUMN age integer;
```

This command will not return any output.

## Code explanation


- `ALTER TABLE`: The command used to alter a table in PostgreSQL
- `table_name`: The name of the table you want to alter
- `ADD COLUMN`: The action used to add a new column to a table
- `column_name`: The name of the column you want to add
- `data_type`: The data type of the column you want to add

## Helpful links

- [PostgreSQL Documentation - ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html)

onelinerhub: [How do I add a column to a PostgreSQL table?](https://onelinerhub.com/postgresql/how-do-i-add-a-column-to-a-postgresql-table)