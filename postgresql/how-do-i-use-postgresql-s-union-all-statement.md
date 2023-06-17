# How do I use PostgreSQL's UNION ALL statement?
// plain

The PostgreSQL UNION ALL statement is used to combine the result sets of two or more SELECT statements into a single result set. It does not remove duplicate rows from the result set, unlike the UNION statement.

## Example code

```
SELECT * FROM table1
UNION ALL
SELECT * FROM table2;
```

The example code above will combine the results from both table1 and table2 into a single result set.

## Code explanation

- SELECT: specifies the columns to be returned by the query
- FROM: specifies the table(s) from which to retrieve the data
- UNION ALL: combines the result sets of two or more SELECT statements into a single result set

## Helpful links
- [PostgreSQL Documentation: UNION ALL](https://www.postgresql.org/docs/current/sql-union-all.html)

onelinerhub: [How do I use PostgreSQL's UNION ALL statement?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-union-all-statement)