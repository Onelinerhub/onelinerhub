# How to backup a database in Mariadb?
// plain

Backing up a database in MariaDB is a simple process. To do so, you can use the `mysqldump` command. This command will create a backup of the database in a SQL file.

```
mysqldump -u username -p database_name > backup_file.sql
```

The command above will create a backup of the database `database_name` and save it to the file `backup_file.sql`.

The parts of the command are:
- `mysqldump`: The command to create a backup of the database.
- `-u username`: The username of the user with access to the database.
- `-p`: The password of the user with access to the database.
- `database_name`: The name of the database to be backed up.
- `> backup_file.sql`: The file to save the backup to.

For more information, see the [MariaDB documentation](https://mariadb.com/kb/en/library/mysqldump/).

onelinerhub: [How to backup a database in Mariadb?](https://onelinerhub.com/mariadb/how-to-backup-a-database-in-mariadb)