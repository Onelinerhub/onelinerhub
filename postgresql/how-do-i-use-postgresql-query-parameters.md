# How do I use PostgreSQL query parameters?
// plain

PostgreSQL query parameters are used to pass values to a query at runtime. The basic syntax is to use the `$1`, `$2`, etc. notation for each parameter, and then provide the values in the same order as the parameters when executing the query.

For example, the following query uses two parameters:

```
SELECT * FROM users WHERE name = $1 AND age = $2;
```

The values are then passed in when executing the query:

```
SELECT * FROM users WHERE name = 'John' AND age = 32;
```

The parameters can also be used to pass in table and column names, allowing for dynamic SQL statements. For example:

```
SELECT * FROM $1 WHERE $2 = $3;
```

This can be executed with the following values:

```
SELECT * FROM users WHERE name = 'John';
```

The main benefits of using query parameters are security and performance. By using parameters, the database can cache the query plan, allowing for better performance. Additionally, it prevents SQL injection attacks since the data is passed in separately from the query.

## Helpful links

- [PostgreSQL Documentation on Parameters](https://www.postgresql.org/docs/current/static/sql-syntax-calling-funcs.html#SQL-SYNTAX-VARIABLES)
- [SQL Injection Tutorial](https://www.w3schools.com/sql/sql_injection.asp)

onelinerhub: [How do I use PostgreSQL query parameters?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-query-parameters)