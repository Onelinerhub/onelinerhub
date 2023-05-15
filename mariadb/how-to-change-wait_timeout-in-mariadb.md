# How to change wait_timeout in Mariadb?
// plain

The `wait_timeout` variable in MariaDB can be changed by setting the `wait_timeout` variable in the `my.cnf` configuration file.

## Example code

```
[mysqld]
wait_timeout=60
```

This will set the `wait_timeout` variable to 60 seconds.

## Code explanation

- `[mysqld]` - This is the section of the configuration file where the `wait_timeout` variable should be set.
- `wait_timeout=60` - This is the line that sets the `wait_timeout` variable to 60 seconds.

## Helpful links
- [MariaDB Documentation - Server System Variables](https://mariadb.com/kb/en/library/server-system-variables/)

onelinerhub: [How to change wait_timeout in Mariadb?](https://onelinerhub.com/mariadb/how-to-change-wait_timeout-in-mariadb)