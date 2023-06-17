# How do I use the WITH statement in PostgreSQL?
// plain

The WITH statement in PostgreSQL is a convenient way to write complex queries. It allows you to define a set of subqueries which can then be used in the main query. This makes it easier to read and debug complex queries.

Here is an example of a WITH statement:

```
WITH subquery1 AS (
    SELECT *
    FROM table1
),
subquery2 AS (
    SELECT *
    FROM table2
)
SELECT *
FROM subquery1
JOIN subquery2
ON subquery1.id = subquery2.id;
```

This query consists of two subqueries, `subquery1` and `subquery2`, which are defined in the `WITH` clause. These subqueries are then used in the main `SELECT` statement.

## Code explanation


1. `WITH` clause: This is where the subqueries are defined.
2. Subqueries: These are the queries that are defined in the `WITH` clause.
3. `SELECT` statement: This is the main query that uses the subqueries defined in the `WITH` clause.

## Helpful links

- [PostgreSQL Documentation on WITH](https://www.postgresql.org/docs/9.1/queries-with.html)
- [W3Schools Tutorial on PostgreSQL WITH](https://www.w3schools.com/sql/sql_with.asp)

onelinerhub: [How do I use the WITH statement in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-use-the-with-statement-in-postgresql)