# How do I create a backup of my PostgreSQL database?
// plain

Creating a backup of a PostgreSQL database is done using the `pg_dump` command. This command will create a backup file of the specified database.

## Example

```
$ pg_dump mydb > db_backup.sql
```

This will create a backup of the `mydb` database in the file `db_backup.sql`.

The `pg_dump` command has several options to customize the output of the backup file. For example, the `-F` option can be used to specify the format of the output file, such as `-Fc` for a custom format or `-Fp` for a plain-text SQL file.

## Code explanation

- `pg_dump`: The command used to create the backup.
- `mydb`: The name of the database to be backed up.
- `db_backup.sql`: The file that the backup will be saved to.
- `-F`: Option to specify the format of the output file.

## Helpful links
- [PostgreSQL Documentation: pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)

onelinerhub: [How do I create a backup of my PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-create-a-backup-of-my-postgresql-database-1686970390)