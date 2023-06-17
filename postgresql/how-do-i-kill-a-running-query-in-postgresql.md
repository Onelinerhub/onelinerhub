# How do I kill a running query in PostgreSQL?
// plain

To kill a running query in PostgreSQL, use the `pg_cancel_backend()` function. This function takes a single argument, the `pid` of the query to be killed. For example, to kill a query with `pid` of 123:

```
SELECT pg_cancel_backend(123);
```

The output of this command will be `t` if the query was successfully killed, and `f` if not.

## Code explanation


- `pg_cancel_backend()`: This is the function used to kill a running query.
- `pid`: This is the process ID of the query to be killed.
- `SELECT`: This is the SQL statement used to execute the `pg_cancel_backend()` function.

## Helpful links
- [pg_cancel_backend()](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-SIGNAL-TABLE)

onelinerhub: [How do I kill a running query in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-kill-a-running-query-in-postgresql)