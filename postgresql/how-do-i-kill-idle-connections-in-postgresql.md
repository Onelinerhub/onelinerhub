# How do I kill idle connections in PostgreSQL?
// plain

Using the pg_terminate_backend() function, you can kill idle connections in PostgreSQL.

```
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'DBNAME'
  AND state = 'idle';
```

This query will terminate all idle connections in the database.

The parts of the query are as follows:
- `SELECT pg_terminate_backend(pid)` - This part of the query will terminate the backend process.
- `FROM pg_stat_activity` - This part of the query will get the list of processes from the `pg_stat_activity` view.
- `WHERE datname = 'DBNAME'` - This part of the query will filter the results by the database name.
- `AND state = 'idle'` - This part of the query will filter the results by the state of the connection.

For more information, please refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/).

onelinerhub: [How do I kill idle connections in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-kill-idle-connections-in-postgresql)