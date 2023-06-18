# How do I use a SQLite client to access a database?
// plain

1. Install a SQLite client, such as [DB Browser for SQLite](https://sqlitebrowser.org/).
2. Launch the client, and select `File > Open Database` to open an existing database or `File > Create Database` to create a new one.
3. Once the database is open, you can execute SQL commands by typing them into the query window and clicking the `Play` button.
4. For example, to list all tables in the database, you can run the `SELECT name FROM sqlite_master WHERE type='table'` statement:

```sql
SELECT name FROM sqlite_master WHERE type='table';
```

## Output example

```
table1
table2
table3
```

5. To view the data in a table, you can use the `SELECT * FROM table_name` statement:

```sql
SELECT * FROM table1;
```

## Output example

```
field1 | field2 | field3
-----------------------------
value1 | value2 | value3
value4 | value5 | value6
```

6. You can also use the client to create, modify, and delete tables and records.
7. For more information on SQLite and how to use it, see the [SQLite Documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How do I use a SQLite client to access a database?](https://onelinerhub.com/sqlite/how-do-i-use-a-sqlite-client-to-access-a-database)