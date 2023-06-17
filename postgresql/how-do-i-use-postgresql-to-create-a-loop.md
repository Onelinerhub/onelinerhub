# How do I use PostgreSQL to create a loop?
// plain

PostgreSQL does not support loops, but it does offer alternatives. One way to achieve the same result as a loop is to use a recursive CTE (Common Table Expression). A recursive CTE allows you to reference itself, and then use the result of that query to create a new result.

For example, the following query will create a table with the numbers 1 to 10:
```
WITH RECURSIVE cte (n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1
  FROM cte
  WHERE n < 10
)
SELECT * FROM cte;
```

## Output example

```
 n
---
 1
 2
 3
 4
 5
 6
 7
 8
 9
 10
(10 rows)
```

The code can be broken down as follows:
* `WITH RECURSIVE cte (n)` - This declares the CTE named `cte` with column `n`
* `SELECT 1` - This is the base case, which is used to start the recursive query
* `UNION ALL` - This combines the results of the recursive query and the base case
* `SELECT n + 1` - This is the recursive part of the query, which adds 1 to the value of `n`
* `FROM cte` - This references the CTE itself
* `WHERE n < 10` - This is the termination condition, which stops the recursive query when `n` is 10
* `SELECT * FROM cte` - This is the final query which selects all the results from the CTE

For more information, see the following links:
* [PostgreSQL Documentation - Recursive Queries Using WITH](https://www.postgresql.org/docs/current/queries-with.html)
* [W3Schools - PostgreSQL Common Table Expressions](https://www.w3schools.com/sql/sql_cte.asp)

onelinerhub: [How do I use PostgreSQL to create a loop?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-to-create-a-loop)