# How do I create a database in PostgreSQL?
// plain

Creating a database in PostgreSQL is a simple process. To create a new database, use the following code:

```
CREATE DATABASE database_name;
```

This will create a new database with the given name.

The code consists of the following parts:

1. `CREATE DATABASE` - This is the command used to create a new database.
2. `database_name` - This is the name of the database you want to create.

Once the database is created, you can use the `\l` command to list all the databases present in the server.

```
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 database_name | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
(2 rows)
```

The database is now created and ready to be used.

For more information on creating databases in PostgreSQL, please refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/current/sql-createdatabase.html).

onelinerhub: [How do I create a database in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-a-database-in-postgresql)