# How do I view the PostgreSQL query log?
// plain

The PostgreSQL query log is a log file that records all queries that have been run against a PostgreSQL database server. It can be used to diagnose and troubleshoot issues with the database server and queries.

To view the query log, you can use the `pg_log` command. This command takes the path to the log file as an argument, and prints the contents of the log to the terminal.

For example, if the log file is located at `/var/log/postgresql/postgresql.log`, you can view it with the command:

```
$ pg_log /var/log/postgresql/postgresql.log
```

The output of this command will be the contents of the log file. This will include entries for each query that has been run, including the time it was run, the user who ran it, and the query itself.

You can also use the `tail` command to view the last few entries in the log file. This can be useful if you only want to see the most recent queries that have been run.

For example, to view the last 10 entries in the log file, you can use the command:

```
$ tail -n 10 /var/log/postgresql/postgresql.log
```

The output of this command will be the last 10 entries in the log file.

Alternatively, you can use a log viewer such as [pgBadger](https://github.com/dalibo/pgbadger) to view the query log in a more user-friendly format.

### List of Code Parts

1. `pg_log`: Command to view the query log
2. `/var/log/postgresql/postgresql.log`: Path to the log file
3. `tail`: Command to view the last few entries in the log file
4. `tail -n 10 /var/log/postgresql/postgresql.log`: Command to view the last 10 entries in the log file

### Relevant Links

- [pgBadger](https://github.com/dalibo/pgbadger): Log viewer for PostgreSQL query logs

onelinerhub: [How do I view the PostgreSQL query log?](https://onelinerhub.com/postgresql/how-do-i-view-the-postgresql-query-log)