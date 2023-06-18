# How do I use SQLite VACUUM to reclaim disk space?
// plain

SQLite VACUUM is a command used to reclaim disk space by removing all free pages from a database file. This will reduce the size of the database file and free up disk space. To use this command, use the following example code:

```
sqlite> VACUUM;
```

This will run the VACUUM command on the current database. There is no output associated with the VACUUM command.

## Code explanation


- `VACUUM`: This is the command used to reclaim disk space by removing all free pages from a database file.

## Helpful links

- [SQLite VACUUM Command](https://www.sqlite.org/lang_vacuum.html)
- [SQLite VACUUM Tutorial](https://www.sqlitetutorial.net/sqlite-vacuum/)

onelinerhub: [How do I use SQLite VACUUM to reclaim disk space?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-vacuum-to-reclaim-disk-space)