# How can I limit the results returned by a PostgreSQL query?
// plain

Limiting the results returned by a PostgreSQL query can be done with the `LIMIT` clause. This clause is used to restrict the number of rows returned in a query result. For example:

```
SELECT * FROM table_name
LIMIT 5;
```

This query will return only the first 5 rows from the table.

The `LIMIT` clause can also be used in combination with the `OFFSET` clause to skip a number of rows before starting to return the results. For example:

```
SELECT * FROM table_name
LIMIT 5
OFFSET 10;
```

This query will return the rows 11 through 15 from the table.

The parts of the code used in the examples are:

* `SELECT` - specifies the columns to be returned by the query
* `FROM` - specifies the table from which the data is to be retrieved
* `LIMIT` - specifies the maximum number of rows to be returned
* `OFFSET` - specifies the number of rows to be skipped before returning the results

For more information, please see the [PostgreSQL documentation](https://www.postgresql.org/docs/9.3/queries-limit.html).

onelinerhub: [How can I limit the results returned by a PostgreSQL query?](https://onelinerhub.com/postgresql/how-can-i-limit-the-results-returned-by-a-postgresql-query)