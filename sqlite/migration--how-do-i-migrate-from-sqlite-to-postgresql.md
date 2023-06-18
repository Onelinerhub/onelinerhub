# migration

How do I migrate from SQLite to Postgresql?
// plain

Migrating from SQLite to Postgresql requires a few steps.

1. Create a dump of the SQLite database using the following command:

```
sqlite3 database.db .dump > dump.sql
```

2. Create a Postgresql database and user to use.

3. Import the dump into the Postgresql database using the following command:

```
psql -U postgres -d postgres_db < dump.sql
```

4. Confirm the data has been imported correctly by querying the tables.

5. Update the connection string of your application to point to the Postgresql database.

6. Test the application to ensure the data is being accessed correctly.

7. Clean up any resources created during the migration process.

## Helpful links

- [Migrating from SQLite to Postgresql](https://www.digitalocean.com/community/tutorials/how-to-migrate-from-sqlite-to-postgresql-on-ubuntu-18-04)
- [SQLite .dump command](https://www.sqlite.org/cli.html#dot_dot_commands)
- [Postgresql psql command](https://www.postgresql.org/docs/9.2/app-psql.html)

onelinerhub: [migration

How do I migrate from SQLite to Postgresql?](https://onelinerhub.com/sqlite/migration--how-do-i-migrate-from-sqlite-to-postgresql)