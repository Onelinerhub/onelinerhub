# How do I install and configure PostgreSQL on a Windows machine?
// plain

1. Download and install the latest version of PostgreSQL from the [official website](https://www.postgresql.org/download/windows/).
2. Create a database cluster by running the command `initdb -D "C:\Program Files\PostgreSQL\12\data"` in the terminal.
3. Start the PostgreSQL server by running the command `pg_ctl -D "C:\Program Files\PostgreSQL\12\data" -l logfile start`.
4. Connect to the server using the command `psql -h localhost -U postgres` and create a new database with the command `CREATE DATABASE mydb;`.
5. Configure the authentication settings in the pg_hba.conf file located in the data directory.
6. Set up the database connection by editing the postgresql.conf file located in the data directory.
7. Restart the server by running the command `pg_ctl -D "C:\Program Files\PostgreSQL\12\data" -l logfile restart` to apply the changes.

Example code block:
```
CREATE DATABASE mydb;
```

No output.

onelinerhub: [How do I install and configure PostgreSQL on a Windows machine?](https://onelinerhub.com/postgresql/how-do-i-install-and-configure-postgresql-on-a-windows-machine)