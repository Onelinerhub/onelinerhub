# How can I view my PostgreSQL query history?
// plain

You can view your PostgreSQL query history by using the `psql` command-line interface. The `\s` command will show you the history of queries that have been run in the current session.

For example:

```
postgres=# \s
                                              List of relations
 Schema |         Name          | Type  |  Owner
--------+-----------------------+-------+----------
 public | accounts              | table | postgres
 public | customers             | table | postgres
 public | orders                | table | postgres
(3 rows)

postgres=# select * from accounts;
 id |  name  | balance
----+--------+---------
  1 | Alice  |   1000
  2 | Bob    |   2000
(2 rows)

postgres=# \s
                                              List of relations
 Schema |         Name          | Type  |  Owner
--------+-----------------------+-------+----------
 public | accounts              | table | postgres
 public | customers             | table | postgres
 public | orders                | table | postgres
(3 rows)

History of queries run in this session:
  1. select * from accounts;
```

The `\s` command will show you the history of queries that have been run in the current session, including the query number, the query itself, and the time it was run. You can also use the `\h` command to view the syntax of a query that has been run previously.

## Code explanation

1. `psql` command-line interface - This is a command-line interface for interacting with PostgreSQL databases.
2. `\s` command - This command will show you the history of queries that have been run in the current session.
3. `\h` command - This command will show you the syntax of a query that has been run previously.

## Helpful links
1. [PostgreSQL Documentation - psql Command Line Tool](https://www.postgresql.org/docs/current/app-psql.html)
2. [PostgreSQL Documentation - psql Special Commands](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-SPECIAL-COMMANDS)

onelinerhub: [How can I view my PostgreSQL query history?](https://onelinerhub.com/postgresql/how-can-i-view-my-postgresql-query-history)