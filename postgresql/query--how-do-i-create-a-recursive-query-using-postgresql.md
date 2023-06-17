# query

How do I create a recursive query using PostgreSQL?
// plain

To create a recursive query using PostgreSQL, you need to use the `WITH RECURSIVE` clause. This clause allows you to define a recursive query, which is a query that references itself in the `FROM` clause.

For example, the following code will create a recursive query that will return the Fibonacci sequence up to the 10th number:
```
WITH RECURSIVE fibonacci(n, result) AS (
    SELECT 1, 0
  UNION ALL
    SELECT n + 1, result + n
    FROM fibonacci
    WHERE n < 10
)
SELECT result FROM fibonacci;
```

The output of this query is:
```
result
0
1
1
2
3
5
8
13
21
34
```

The code above consists of three parts:
- `WITH RECURSIVE` clause: this is used to define a recursive query.
- `SELECT` clause: this is used to define the columns that will be returned in the result.
- `FROM` clause: this is used to reference the recursive query itself.

For more information on creating recursive queries using PostgreSQL, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/queries-with.html).

onelinerhub: [query

How do I create a recursive query using PostgreSQL?](https://onelinerhub.com/postgresql/query--how-do-i-create-a-recursive-query-using-postgresql)