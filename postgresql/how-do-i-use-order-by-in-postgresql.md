# How do I use ORDER BY in PostgreSQL?
// plain

The `ORDER BY` clause is used in PostgreSQL to sort the result set of a `SELECT` statement. It is used to specify the order in which the rows of a table are returned.

For example:

```
SELECT * FROM table ORDER BY column1, column2;
```

This statement will return the rows of the table sorted by `column1` and then by `column2`.

You can also specify the order in which the results are returned. To do this, you can use the `ASC` and `DESC` keywords. For example:

```
SELECT * FROM table ORDER BY column1 ASC, column2 DESC;
```

This statement will return the rows of the table sorted in ascending order by `column1` and in descending order by `column2`.

You can also use expressions in the `ORDER BY` clause. For example:

```
SELECT * FROM table ORDER BY ABS(column1) + column2;
```

This statement will return the rows of the table sorted by the expression `ABS(column1) + column2`.

You can also use multiple `ORDER BY` clauses in a single statement. For example:

```
SELECT * FROM table ORDER BY column1, column2 ORDER BY column3;
```

This statement will return the rows of the table sorted by `column1` and `column2` first and then by `column3`.

You can find more information about `ORDER BY` in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-select.html#SQL-ORDERBY).

onelinerhub: [How do I use ORDER BY in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-use-order-by-in-postgresql)