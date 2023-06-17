# How do I view PostgreSQL logs?
// plain

To view PostgreSQL logs, you need to access the log files located in the `data/pg_log` directory.

For example, you can use the following command to view the log file:
```
$ cat data/pg_log/postgresql-Sat.log
```

The output will contain the log entries of the PostgreSQL server.

The parts of the command are as follows:

1. `cat` - the command used to view the contents of a text file
2. `data/pg_log/postgresql-Sat.log` - the path to the log file

You can also use other commands like `tail` to view the last few lines of the log file.

```
$ tail data/pg_log/postgresql-Sat.log
```

For more information, you can refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-logging.html).

onelinerhub: [How do I view PostgreSQL logs?](https://onelinerhub.com/postgresql/how-do-i-view-postgresql-logs)