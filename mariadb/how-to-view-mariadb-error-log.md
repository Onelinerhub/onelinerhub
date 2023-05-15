# How to view Mariadb error log?
// plain

The MariaDB error log can be viewed using the `mysqld` command. This command will display the error log in the terminal window.

## Example

```
mysqld --log-error=/var/log/mysql/error.log
```

## Output example

```
[Note] mysqld: ready for connections.
Version: '10.3.22-MariaDB-0+deb10u1'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

The command has the following parts:

- `mysqld`: This is the MariaDB server daemon.
- `--log-error`: This is the option to specify the location of the error log.
- `/var/log/mysql/error.log`: This is the path to the error log file.

## Helpful links

- [MariaDB Documentation: Logging](https://mariadb.com/kb/en/library/logging/)

onelinerhub: [How to view Mariadb error log?](https://onelinerhub.com/mariadb/how-to-view-mariadb-error-log)