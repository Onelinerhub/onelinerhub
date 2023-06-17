# How do I use PostgreSQL to filter data?
// plain

PostgreSQL provides a powerful set of tools for filtering data. To filter data with PostgreSQL, the `SELECT` statement is used. For example, to filter a table for all records where the value in the `name` column is equal to `John`, the following statement can be used:

```
SELECT * FROM users WHERE name = 'John';
```

This statement will return all records from the `users` table where the value in the `name` column is equal to `John`.

The `SELECT` statement can also be used to filter data based on multiple criteria. For example, to filter a table for all records where the value in the `name` column is equal to `John` and the value in the `age` column is greater than or equal to `20`, the following statement can be used:

```
SELECT * FROM users WHERE name = 'John' AND age >= 20;
```

This statement will return all records from the `users` table where the value in the `name` column is equal to `John` and the value in the `age` column is greater than or equal to `20`.

The `SELECT` statement can also be used to filter data using comparison operators such as `LIKE` and `IN`. For example, to filter a table for all records where the value in the `name` column is equal to `John` or `Jane`, the following statement can be used:

```
SELECT * FROM users WHERE name IN ('John', 'Jane');
```

This statement will return all records from the `users` table where the value in the `name` column is equal to `John` or `Jane`.

In summary, PostgreSQL provides a powerful set of tools for filtering data. The `SELECT` statement is used to filter data based on criteria specified in the `WHERE` clause. Comparison operators such as `LIKE` and `IN` can also be used to filter data.

## Helpful links

- [PostgreSQL Documentation on SELECT](https://www.postgresql.org/docs/current/sql-select.html)
- [PostgreSQL Documentation on WHERE](https://www.postgresql.org/docs/current/sql-select.html#SQL-WHERE)

onelinerhub: [How do I use PostgreSQL to filter data?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-to-filter-data)