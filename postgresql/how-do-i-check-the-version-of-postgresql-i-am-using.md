# How do I check the version of PostgreSQL I am using?
// plain

To check the version of PostgreSQL you are using, you can use the `SELECT` statement with the `version()` function. This will return the version of PostgreSQL you are running.

For example:

```
SELECT version();
```

## Output example


```
PostgreSQL 10.12 on x86_64-apple-darwin17.7.0, compiled by Apple LLVM version 10.0.1 (clang-1001.0.46.4), 64-bit
```

The code consists of:

- `SELECT` statement - used to select data from a database
- `version()` function - used to return the version of PostgreSQL you are running

## Helpful links

- [PostgreSQL Documentation - SELECT Statement](https://www.postgresql.org/docs/current/sql-select.html)
- [PostgreSQL Documentation - version() Function](https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-VERSION)

onelinerhub: [How do I check the version of PostgreSQL I am using?](https://onelinerhub.com/postgresql/how-do-i-check-the-version-of-postgresql-i-am-using)