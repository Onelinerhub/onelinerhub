# How can I extract data from a PostgreSQL database?
// plain

To extract data from a PostgreSQL database, you can use the `SELECT` statement to query the database.

For example, to select all columns from the 'users' table:

```sql
SELECT * FROM users;
```

The output of this query would be the data from the 'users' table.

To select specific columns from the 'users' table, specify the columns after the `SELECT` keyword:

```sql
SELECT name, email FROM users;
```

The output of this query would be the 'name' and 'email' columns from the 'users' table.

To filter the results, you can use the `WHERE` clause to specify the conditions for the query:

```sql
SELECT name, email FROM users WHERE age > 18;
```

The output of this query would be the 'name' and 'email' columns from the 'users' table for users with an age greater than 18.

You can also use `ORDER BY` to sort the results and `LIMIT` to limit the number of results:

```sql
SELECT name, email FROM users WHERE age > 18 ORDER BY name LIMIT 10;
```

The output of this query would be the first 10 'name' and 'email' columns from the 'users' table for users with an age greater than 18 sorted by name.

Parts of the query:

- `SELECT`: The keyword used to select the columns from the table.
- `FROM`: The keyword used to specify the table from which to select the data.
- `WHERE`: The keyword used to filter the results based on certain conditions.
- `ORDER BY`: The keyword used to sort the results.
- `LIMIT`: The keyword used to limit the number of results.

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SELECT Statement](https://www.postgresql.org/docs/current/sql-select.html)
- [WHERE Clause](https://www.postgresql.org/docs/current/sql-select.html#SQL-WHERE)
- [ORDER BY Clause](https://www.postgresql.org/docs/current/sql-select.html#SQL-ORDERBY)
- [LIMIT Clause](https://www.postgresql.org/docs/current/sql-select.html#SQL-LIMIT)

onelinerhub: [How can I extract data from a PostgreSQL database?](https://onelinerhub.com/postgresql/how-can-i-extract-data-from-a-postgresql-database)