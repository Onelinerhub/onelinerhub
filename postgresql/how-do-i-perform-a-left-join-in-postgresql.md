# How do I perform a left join in PostgreSQL?
// plain

A left join in PostgreSQL is used to combine two tables by matching values from the left table with values from the right table. It returns all rows from the left table, even if there are no matches in the right table.

The syntax for a left join in PostgreSQL is as follows:

```
SELECT *
FROM table_1
LEFT JOIN table_2
ON table_1.column_1 = table_2.column_1
```

This example code will return all rows from table_1 and any matching rows from table_2.

The parts of the code are:

- `SELECT *`: This selects all columns from the tables.
- `FROM table_1`: This specifies the left table.
- `LEFT JOIN table_2`: This specifies the type of join to use.
- `ON table_1.column_1 = table_2.column_1`: This specifies the join condition.

## Helpful links

- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/sql-select.html#SQL-FROM)
- [W3Schools SQL LEFT JOIN](https://www.w3schools.com/sql/sql_join_left.asp)

onelinerhub: [How do I perform a left join in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-perform-a-left-join-in-postgresql)