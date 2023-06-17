# How do I change the data type of a column in PostgreSQL?
// plain

To change the data type of a column in PostgreSQL, you will need to use the ALTER TABLE command. This command allows you to modify the structure of an existing table.

For example, to change the data type of the "name" column of the "users" table from varchar(255) to text, you could use the following command:

```
ALTER TABLE users ALTER COLUMN name TYPE text;
```

This command will not display any output.

The parts of this command are as follows:

- `ALTER TABLE`: This statement is used to modify the structure of an existing table.
- `users`: This is the name of the table that you want to modify.
- `ALTER COLUMN`: This statement is used to modify the structure of an existing column.
- `name`: This is the name of the column that you want to modify.
- `TYPE`: This statement is used to specify the new data type for the column.
- `text`: This is the new data type for the column.

For more information on the ALTER TABLE command, you can refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/9.1/sql-altertable.html).

onelinerhub: [How do I change the data type of a column in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-change-the-data-type-of-a-column-in-postgresql)