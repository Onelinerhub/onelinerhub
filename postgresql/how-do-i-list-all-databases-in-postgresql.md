# How do I list all databases in PostgreSQL?
// plain

To list all databases in PostgreSQL, you can run the following command:

```
\l
```

This will return a list of all databases available in the PostgreSQL server. The output will look something like this:

```
                                      List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)
```

The command `\l` is an alias for the `\list` command. This command can take an optional parameter `pattern` to filter the list of databases by name. For example, to list only databases that start with the letter `a`, you can use the following command:

```
\l a%
```

This will output only the databases that start with the letter `a`.

For more information, please refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/9.5/sql-createdatabase.html).

onelinerhub: [How do I list all databases in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-list-all-databases-in-postgresql)