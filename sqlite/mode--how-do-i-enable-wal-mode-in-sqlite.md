# mode

How do I enable WAL mode in SQLite?
// plain

In order to enable WAL mode in SQLite, you need to execute the following command:

```sql
PRAGMA journal_mode=WAL;
```

This will enable the WAL (Write-Ahead Logging) mode in SQLite. In WAL mode, all changes to the database are written to a separate log file (the WAL file) instead of being written directly to the database file. This allows for faster and more efficient transactions, as well as improved concurrency.

The code consists of the following parts:

1. **PRAGMA**: This is an SQLite command that is used to set various parameters.
2. **journal_mode**: This is the parameter that is being set.
3. **WAL**: This is the value that is being set for the parameter. It stands for Write-Ahead Logging.

The output of the above command should be:

```
PRAGMA journal_mode=WAL;
```

The above command will enable WAL mode in SQLite.

## Helpful links

- [SQLite Write-Ahead Logging](https://www.sqlite.org/wal.html)
- [SQLite PRAGMA](https://www.sqlite.org/pragma.html)

onelinerhub: [mode

How do I enable WAL mode in SQLite?](https://onelinerhub.com/sqlite/mode--how-do-i-enable-wal-mode-in-sqlite)