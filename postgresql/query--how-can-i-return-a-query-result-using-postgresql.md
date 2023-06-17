# query

How can I return a query result using PostgreSQL?
// plain

PostgreSQL provides a powerful query language to return query results. This can be done using the `SELECT` statement. The syntax is as follows:

```
SELECT [column(s)]
FROM [table(s)]
WHERE [condition(s)];
```

For example, to return all the rows from a table called `employees`:

```
SELECT *
FROM employees;
```

This will return all the columns and rows from the `employees` table.

The `SELECT` statement can also be used to filter the results. For example, to return only the rows where the `salary` is greater than 5000:

```
SELECT *
FROM employees
WHERE salary > 5000;
```

This will return all the columns and rows from the `employees` table where the `salary` is greater than 5000.

The `SELECT` statement can also be used to sort the results. For example, to sort the results by `salary` in descending order:

```
SELECT *
FROM employees
ORDER BY salary DESC;
```

This will return all the columns and rows from the `employees` table sorted by `salary` in descending order.

To learn more about using the `SELECT` statement in PostgreSQL, please refer to the official documentation [here](https://www.postgresql.org/docs/current/sql-select.html).

onelinerhub: [query

How can I return a query result using PostgreSQL?](https://onelinerhub.com/postgresql/query--how-can-i-return-a-query-result-using-postgresql)