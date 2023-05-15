# How to backup a table in Mariadb?
// plain

Backing up a table in MariaDB is a simple process. To do so, you can use the `mysqldump` command. This command will create a backup of the table in the form of a SQL script.

## Example

```
mysqldump -u username -p database_name table_name > backup.sql
```

This command will create a backup of the table named `table_name` from the database `database_name` and save it to the file `backup.sql`.

The parts of the command are:
- `mysqldump`: The command to create a backup of a table.
- `-u username`: The username used to connect to the database.
- `-p`: The password used to connect to the database.
- `database_name`: The name of the database containing the table.
- `table_name`: The name of the table to be backed up.
- `> backup.sql`: The file to save the backup to.

## Helpful links
- [MariaDB Documentation - mysqldump](https://mariadb.com/kb/en/library/mysqldump/)

onelinerhub: [How to backup a table in Mariadb?](https://onelinerhub.com/mariadb/how-to-backup-a-table-in-mariadb)