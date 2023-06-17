# query

How do I write a PostgreSQL SELECT query?
// plain

A PostgreSQL SELECT query is used to retrieve data from a table in a database. The basic syntax of a SELECT query is as follows:

```
SELECT column_name1, column_name2
FROM table_name
WHERE condition;
```

The `SELECT` keyword is used to specify the columns in the table that should be returned. The `FROM` keyword is used to specify the table from which the data should be retrieved. The `WHERE` clause can be used to specify a condition that must be met in order for a row to be returned.

The following example shows a SELECT query that returns all rows from the `users` table where the `age` column is greater than 18:

```
SELECT name, age
FROM users
WHERE age > 18;
```

This query will return a result set containing the `name` and `age` columns from the `users` table where the age is greater than 18.

For more information on SELECT queries in PostgreSQL, please refer to the [PostgreSQL SELECT documentation](https://www.postgresql.org/docs/current/sql-select.html).

onelinerhub: [query

How do I write a PostgreSQL SELECT query?](https://onelinerhub.com/postgresql/query--how-do-i-write-a-postgresql-select-query)