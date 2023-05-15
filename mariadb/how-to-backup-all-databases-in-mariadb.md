# How to backup all databases in Mariadb?
// plain

Backing up all databases in MariaDB can be done using the `mysqldump` command. This command will create a backup of all databases in the form of a SQL script.

## Example

```
mysqldump --all-databases > all_databases.sql
```

This command will create a file called `all_databases.sql` which contains the SQL script for all databases.

## Code explanation

- `mysqldump`: The command used to create a backup of all databases.
- `--all-databases`: An option to specify that all databases should be backed up.
- `> all_databases.sql`: The output of the command will be written to the file `all_databases.sql`.

## Helpful links
- [MariaDB Documentation - mysqldump](https://mariadb.com/kb/en/library/mysqldump/)

onelinerhub: [How to backup all databases in Mariadb?](https://onelinerhub.com/mariadb/how-to-backup-all-databases-in-mariadb)