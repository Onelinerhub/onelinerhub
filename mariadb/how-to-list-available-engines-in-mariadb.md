# How to list available engines in Mariadb?
// plain

To list available engines in Mariadb, you can use the `SHOW ENGINES` command. This command will display a list of all available storage engines and their status.

## Example

```
MariaDB [(none)]> SHOW ENGINES;
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                        | Transactions | XA   | Savepoints |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| CSV                | YES     | CSV storage engine                                             | NO           | NO   | NO         |
| InnoDB             | DEFAULT | Supports transactions, row-level locking, and foreign keys     | YES          | YES  | YES        |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables      | NO           | NO   | NO         |
| MyISAM             | YES     | MyISAM storage engine                                          | NO           | NO   | NO         |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                             | NO           | NO   | NO         |
| Aria               | YES     | Crash-safe tables with MyISAM heritage                         | NO           | NO   | NO         |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
7 rows in set (0.00 sec)
```

The output of the command will show the engine name, support status, comment, transactions, XA, and savepoints.

The `Support` column will indicate whether the engine is supported or not. The `Comment` column will provide a brief description of the engine. The `Transactions` column will indicate whether the engine supports transactions or not. The `XA` column will indicate whether the engine supports XA transactions or not. The `Savepoints` column will indicate whether the engine supports savepoints or not.

## Helpful links

- [MariaDB Documentation - SHOW ENGINES](https://mariadb.com/kb/en/library/show-engines/)

onelinerhub: [How to list available engines in Mariadb?](https://onelinerhub.com/mariadb/how-to-list-available-engines-in-mariadb)