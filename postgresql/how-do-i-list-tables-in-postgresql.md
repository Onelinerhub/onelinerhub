# How do I list tables in PostgreSQL?
// plain

To list tables in PostgreSQL, you can use the `\dt` command. This command will list all the tables in the current database.

For example:
```
\dt
```

This will output a list of the tables in the current database, along with their schemas and sizes in kilobytes.

```
List of relations
 Schema |      Name      | Type  |  Owner
--------+----------------+-------+---------
 public | mytable        | table | username
 public | myothertable   | table | username
(2 rows)
```

In addition to `\dt`, you can also use `\d` to list all the objects in the current database, including tables, views, functions, and other objects.

For example:
```
\d
```

This will output a list of all the objects in the current database, along with their types, schemas, sizes, and other information.

```
                 List of relations
 Schema |      Name      | Type  |  Owner
--------+----------------+-------+---------
 public | mytable        | table | username
 public | myothertable   | table | username
 public | myview         | view  | username
 public | myfunction     | func  | username
(4 rows)
```

For more information, see the [PostgreSQL Documentation](https://www.postgresql.org/docs/current/sql-dt.html) and the [PostgreSQL Command Line Cheat Sheet](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546).

onelinerhub: [How do I list tables in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-list-tables-in-postgresql)