# How do I use PostgreSQL UNION to combine the results of two queries?
// plain

The PostgreSQL `UNION` statement is used to combine the results of two or more queries into a single result set.

```
SELECT column_name(s)
FROM table1
UNION
SELECT column_name(s)
FROM table2;
```

For example, if you have two tables `table1` and `table2` with the same columns, you can combine the results of both tables into a single result set like this:

```
SELECT column_name
FROM table1
UNION
SELECT column_name
FROM table2;
```

The output of the query would look like this:
```
column_name
-----------
value1
value2
value3
value4
```

The `UNION` statement can also be used to combine results from multiple tables with different columns, but the number of columns and data types must be the same for each query.

You can also use the `UNION ALL` statement to combine multiple queries and include duplicate rows in the results.

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/queries-union.html)
- [W3Schools PostgreSQL Tutorial](https://www.w3schools.com/sql/sql_union.asp)

onelinerhub: [How do I use PostgreSQL UNION to combine the results of two queries?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-union-to-combine-the-results-of-two-queries)