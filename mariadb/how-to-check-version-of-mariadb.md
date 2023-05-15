# How to check version of Mariadb?
// plain

To check the version of MariaDB, you can use the `SELECT VERSION()` command. This command will return the version of MariaDB that is currently running.

## Example

```
mysql> SELECT VERSION();
+-----------------+
| VERSION()       |
+-----------------+
| 10.4.13-MariaDB |
+-----------------+
1 row in set (0.001 sec)
```

The `SELECT VERSION()` command consists of the following parts:

- `SELECT`: This is a keyword used to retrieve data from a database.
- `VERSION()`: This is a function that returns the version of MariaDB that is currently running.

For more information, please refer to the following link:

- [MariaDB Documentation: SELECT VERSION()](https://mariadb.com/kb/en/library/select-version/)

onelinerhub: [How to check version of Mariadb?](https://onelinerhub.com/mariadb/how-to-check-version-of-mariadb)