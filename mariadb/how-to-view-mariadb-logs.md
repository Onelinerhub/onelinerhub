# How to view Mariadb logs?
// plain

Mariadb logs can be viewed using the `mysqld.log` file. This file is located in the `/var/log/mysql` directory. To view the log, use the `tail` command:

```
tail -f /var/log/mysql/mysqld.log
```

This will output the log in real time.

The log contains information about the server, such as startup and shutdown messages, errors, and warnings. It also contains information about queries that have been executed, such as the query text, the user that executed the query, and the time it took to execute.

The log can be used to troubleshoot issues with the server, such as slow queries or connection errors.

## Helpful links

- [Mariadb Documentation - Logging](https://mariadb.com/kb/en/library/logging/)
- [Mariadb Documentation - Troubleshooting](https://mariadb.com/kb/en/library/troubleshooting/)

onelinerhub: [How to view Mariadb logs?](https://onelinerhub.com/mariadb/how-to-view-mariadb-logs)