# How do I view tables in SQLite?
// plain

To view tables in SQLite, you can use the `.tables` command. This will list all the tables in the current database. For example:

```
sqlite> .tables
table1    table2    table3
```

The output of the `.tables` command is a list of all the tables in the current database.

To view the structure of a specific table, you can use the `.schema` command followed by the name of the table. For example:

```
sqlite> .schema table1
CREATE TABLE table1(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER
);
```

The output of the `.schema` command is the SQL statement used to create the table.

To view the contents of a table, you can use the `SELECT` statement. For example:

```
sqlite> SELECT * FROM table1;
1	John	25
2	Jane	30
```

The output of the `SELECT` statement is a list of all the rows in the table.

To view the data type of each column in a table, you can use the `PRAGMA` statement. For example:

```
sqlite> PRAGMA table_info(table1);
0|id|integer|1||1
1|name|text|0||0
2|age|integer|0||0
```

The output of the `PRAGMA` statement is a list of the column names, data types, and other information about the table.

## Helpful links
- [SQLite Documentation - .tables](https://www.sqlite.org/cli.html#tables)
- [SQLite Documentation - .schema](https://www.sqlite.org/cli.html#schema)
- [SQLite Documentation - SELECT](https://www.sqlite.org/lang_select.html)
- [SQLite Documentation - PRAGMA](https://www.sqlite.org/pragma.html)

onelinerhub: [How do I view tables in SQLite?](https://onelinerhub.com/sqlite/how-do-i-view-tables-in-sqlite)