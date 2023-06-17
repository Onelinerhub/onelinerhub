# How do I show databases in PostgreSQL?
// plain

To show databases in PostgreSQL, you can use the `\l` command. This command will list all databases on the server, along with their sizes and owners. For example:

```
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(3 rows)
```

The parts of the code are:

* `\l` - the command to list the databases
* `Name` - the name of the database
* `Owner` - the owner of the database
* `Encoding` - the encoding of the database
* `Collate` - the collation of the database
* `Ctype` - the character type of the database
* `Access privileges` - the access privileges for the database

For more information, you can check out the official PostgreSQL documentation:

* [PostgreSQL Documentation - \l](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS-LIST)

onelinerhub: [How do I show databases in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-show-databases-in-postgresql)