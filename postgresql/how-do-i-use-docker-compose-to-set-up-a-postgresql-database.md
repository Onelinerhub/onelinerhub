# How do I use Docker Compose to set up a PostgreSQL database?
// plain

Using Docker Compose, you can set up a PostgreSQL database in just a few steps.

1. Create a `docker-compose.yml` file with the following contents:
```
version: '3'

services:
  postgres:
    image: postgres:latest
    environment:
      - POSTGRES_PASSWORD=<password>
    ports:
      - 5432:5432
```
This will pull the latest version of PostgreSQL from the Docker Hub and set up a container with the password you specify.

2. Run `docker-compose up` to start the container.

```
Creating network "postgres_default" with the default driver
Creating postgres_postgres_1 ... done
Attaching to postgres_postgres_1
postgres_1  | The files belonging to this database system will be owned by user "postgres".
postgres_1  | This user must also own the server process.
postgres_1  |
postgres_1  | The database cluster will be initialized with locale "en_US.utf8".
postgres_1  | The default database encoding has accordingly been set to "UTF8".
postgres_1  | The default text search configuration will be set to "english".
postgres_1  |
postgres_1  | Data page checksums are disabled.
postgres_1  |
postgres_1  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
postgres_1  | creating subdirectories ... ok
postgres_1  | selecting dynamic shared memory implementation ... posix
postgres_1  | selecting default max_connections ... 100
postgres_1  | selecting default shared_buffers ... 128MB
postgres_1  | selecting default time zone ... Etc/UTC
postgres_1  | creating configuration files ... ok
postgres_1  | running bootstrap script ... ok
postgres_1  | performing post-bootstrap initialization ... ok
postgres_1  | syncing data to disk ... ok
postgres_1  |
postgres_1  | Success. You can now start the database server using:
postgres_1  |
postgres_1  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
postgres_1  |
postgres_1  |
postgres_1  | ****************************************************
postgres_1  | WARNING: No password has been set for the database.
postgres_1  |          This will allow anyone with access to the
postgres_1  |          Postgres port to access your database. In
postgres_1  |          Docker's default configuration, this is
postgres_1  |          effectively any other container on the same
postgres_1  |          system.
postgres_1  |
postgres_1  |          Use "-e POSTGRES_PASSWORD=password" to set
postgres_1  |          it in "docker run".
postgres_1  | ****************************************************
postgres_1  |
postgres_1  | waiting for server to start....2020-04-09 07:17:09.622 UTC [46] LOG:  starting PostgreSQL 12.2 (Debian 12.2-2.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit
postgres_1  | 2020-04-09 07:17:09.622 UTC [46] LOG:  listening on IPv4 address "0.0.0.0", port 5432
postgres_1  | 2020-04-09 07:17:09.622 UTC [46] LOG:  listening on IPv6 address "::", port 5432
postgres_1  | 2020-04-09 07:17:09.634 UTC [46] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres_1  | 2020-04-09 07:17:09.651 UTC [47] LOG:  database system was shut down at 2020-04-09 07:17:09 UTC
postgres_1  | 2020-04-09 07:17:09.668 UTC [46] LOG:  database system is ready to accept connections
```

3. Connect to the database using `docker exec -it <container_name> psql -U postgres`

```
psql (12.2 (Debian 12.2-2.pgdg100+1))
Type "help" for help.

postgres=#
```

4. Create a database by running `CREATE DATABASE <database_name>;`

```
CREATE DATABASE testdb;
CREATE DATABASE
```

5. Connect to the new database by running `\c <database_name>`

```
\c testdb
You are now connected to database "testdb" as user "postgres".
```

6. Verify the database was created by running `\l`

```
                                  List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 testdb    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
(2 rows)
```

You now have a PostgreSQL database running in a Docker container.

**## Helpful links**
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

onelinerhub: [How do I use Docker Compose to set up a PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-use-docker-compose-to-set-up-a-postgresql-database)