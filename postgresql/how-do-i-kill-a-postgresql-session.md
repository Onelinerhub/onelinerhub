# How do I kill a PostgreSQL session?
// plain

You can kill a PostgreSQL session using the `pg_terminate_backend` function. This function requires the process ID (`pid`) of the session you want to terminate.

To get a list of all active sessions, you can use the `pg_stat_activity` view:

```sql
SELECT * FROM pg_stat_activity;
```

The output will look something like this:

```
 pid |  datname  |   usename   | application_name | client_addr | client_hostname | client_port |         backend_start         | backend_xmin | state  | waiting | query
-----+-----------+-------------+------------------+-------------+-----------------+-------------+-------------------------------+--------------+--------+---------+-------
  16 | postgres  | postgres    | psql             | 127.0.0.1   |                 |       57720 | 2020-10-01 17:03:23.483414-07 |              | idle   | f       |
  17 | postgres  | postgres    | psql             | 127.0.0.1   |                 |       57721 | 2020-10-01 17:03:30.874105-07 |              | active | f       | SELECT
(2 rows)
```

Once you have the `pid` of the session you want to terminate, you can use the `pg_terminate_backend` function to terminate it:

```sql
SELECT pg_terminate_backend(17);
```

The output of this command will be `t` if the session was successfully terminated.

For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-SIGNAL-TABLE).

onelinerhub: [How do I kill a PostgreSQL session?](https://onelinerhub.com/postgresql/how-do-i-kill-a-postgresql-session)