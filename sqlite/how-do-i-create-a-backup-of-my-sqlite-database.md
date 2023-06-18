# How do I create a backup of my SQLite database?
// plain

Creating a backup of your SQLite database is a simple process.

1. First, open a terminal window and navigate to the directory where your database is located.
2. Then, use the `.backup` command followed by the name of the backup file and the name of the database you wish to back up.

```
sqlite> .backup my_backup.db my_database.db
```

3. This will create a backup of the database in the same directory, with the name you specified.
4. You can also specify a path for the backup file, if you wish to save it in a different directory.

```
sqlite> .backup /home/user/my_backup.db my_database.db
```

5. If the backup was successful, you should see the following message:

```
Backup completed in 0.063 seconds
```

6. You can also use the `.dump` command to back up your database. This command will create a SQL script of your database, which can be used to re-create the database.

```
sqlite> .dump > my_backup.sql
```

7. To restore the database from the backup, you can use the `.read` command.

```
sqlite> .read my_backup.sql
```

## Helpful links
- [SQLite Backup and Restore](https://www.sqlitetutorial.net/sqlite-backup-restore/)
- [SQLite .backup Command](https://www.sqlitetutorial.net/sqlite-dot-backup-command/)
- [SQLite .dump Command](https://www.sqlitetutorial.net/sqlite-dot-dump-command/)
- [SQLite .read Command](https://www.sqlitetutorial.net/sqlite-dot-read-command/)

onelinerhub: [How do I create a backup of my SQLite database?](https://onelinerhub.com/sqlite/how-do-i-create-a-backup-of-my-sqlite-database)