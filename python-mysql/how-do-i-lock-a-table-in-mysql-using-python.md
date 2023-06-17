# How do I lock a table in MySQL using Python?
// plain

To lock a table in MySQL using Python, you can use the `cursor.execute()` method. This method takes an SQL statement as an argument and executes it. To lock a table, the SQL statement must include the `LOCK TABLES` command.

For example:

```
cursor.execute("LOCK TABLES my_table WRITE;")
```

This will lock the table `my_table` for writing. To unlock the table, use the `UNLOCK TABLES` command:

```
cursor.execute("UNLOCK TABLES;")
```

## Code explanation

- `cursor.execute()`: This method takes an SQL statement as an argument and executes it.
- `LOCK TABLES`: This command is used to lock a table.
- `UNLOCK TABLES`: This command is used to unlock a table.

## Helpful links
- [MySQL Documentation - LOCK TABLES](https://dev.mysql.com/doc/refman/8.0/en/lock-tables.html)
- [MySQL Documentation - UNLOCK TABLES](https://dev.mysql.com/doc/refman/8.0/en/unlock-tables.html)

onelinerhub: [How do I lock a table in MySQL using Python?](https://onelinerhub.com/python-mysql/how-do-i-lock-a-table-in-mysql-using-python)