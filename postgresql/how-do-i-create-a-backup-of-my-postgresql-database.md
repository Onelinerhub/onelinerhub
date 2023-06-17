# How do I create a backup of my PostgreSQL database?
// plain

To create a backup of a PostgreSQL database, the `pg_dump` command can be used. This command takes a snapshot of the database and stores it in a file.

The following example code can be used to create a backup of a PostgreSQL database named "mydb" and store it in a file named "mydb_backup.sql":
```
pg_dump mydb > mydb_backup.sql
```

The code consists of the following parts:
- `pg_dump`: the command to take a backup of the database
- `mydb`: the name of the database to be backed up
- `>`: redirects the output of the command to a file
- `mydb_backup.sql`: the file where the backup will be stored

The output of the command will be the contents of the backup, which will be stored in the file.

For more information, see the [PostgreSQL Documentation](https://www.postgresql.org/docs/current/app-pgdump.html).

onelinerhub: [How do I create a backup of my PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-create-a-backup-of-my-postgresql-database)