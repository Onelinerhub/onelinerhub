# How do I get a list of tables from an SQLite database?
// plain

To get a list of tables from an SQLite database, you can use the `.tables` command. This command will return a list of all the tables in the database. For example, to get a list of tables from the database `my_database.db`:

```
sqlite3 my_database.db
sqlite> .tables
table1
table2
table3
```

This example code connects to the database `my_database.db` and then uses the `.tables` command to get a list of all the tables in the database. The output of this code is a list of the tables in the database, in this case `table1`, `table2`, and `table3`.

The `.tables` command is part of the SQLite command line interface and can be used to get a list of tables from any SQLite database.

## Code explanation

1. `sqlite3 my_database.db` - connects to the `my_database.db` database
2. `.tables` - gets a list of all the tables in the database

## Helpful links
- [SQLite Command Line Interface](https://www.sqlite.org/cli.html)

onelinerhub: [How do I get a list of tables from an SQLite database?](https://onelinerhub.com/sqlite/how-do-i-get-a-list-of-tables-from-an-sqlite-database)