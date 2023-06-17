# How do I connect to a PostgreSQL database using a client?
// plain

1. Install a PostgreSQL client. Popular clients include [psql](https://www.postgresql.org/docs/9.2/app-psql.html) and [pgAdmin](https://www.pgadmin.org/).

2. Connect to the database from the client. The connection details, such as the database name, hostname, port, and user credentials, will be required. For example, to connect to a database named `my_database` on localhost using the default port 5432 with the user `postgres` and the password `my_password`, the following command can be used with the `psql` client:

```
psql -h localhost -U postgres -d my_database -W my_password
```

3. After successful authentication, the following output will be displayed:

```
psql (9.2.24)
Type "help" for help.

postgres=#
```

4. You can now execute SQL statements to interact with the database. For example, to list all the tables in the database, use the `\dt` command:

```
postgres=# \dt
              List of relations
 Schema |      Name       | Type  |  Owner
--------+-----------------+-------+----------
 public | customers       | table | postgres
 public | orders          | table | postgres
 public | products        | table | postgres
(3 rows)
```

5. To disconnect from the database, use the `\q` command:

```
postgres=# \q
```

6. To reconnect to the database, repeat steps 2-5.

7. For more information about connecting to a PostgreSQL database using a client, refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/).

onelinerhub: [How do I connect to a PostgreSQL database using a client?](https://onelinerhub.com/postgresql/how-do-i-connect-to-a-postgresql-database-using-a-client)