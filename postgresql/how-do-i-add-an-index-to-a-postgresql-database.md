# How do I add an index to a PostgreSQL database?
// plain

Adding an index to a PostgreSQL database is a simple process. To do so, you'll need to use the `CREATE INDEX` statement. Here is an example of the syntax:

```
CREATE INDEX index_name ON table_name (column_name);
```

This statement creates an index called `index_name` on the `table_name` table, based on the `column_name` column.

You can also create an index on multiple columns, by separating them with a comma:

```
CREATE INDEX index_name ON table_name (column_name1, column_name2);
```

You can also specify the type of index to create, such as a `UNIQUE` index, which ensures that the values in the index are unique:

```
CREATE UNIQUE INDEX index_name ON table_name (column_name);
```

You can also specify the type of index to create, such as a `BTREE` index, which is the default type of index in PostgreSQL:

```
CREATE INDEX index_name ON table_name USING BTREE (column_name);
```

You can also specify an `INCLUDE` clause to create an index on a subset of columns in a table:

```
CREATE INDEX index_name ON table_name (column_name) INCLUDE (column_name1, column_name2);
```

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-createindex.html).

onelinerhub: [How do I add an index to a PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-add-an-index-to-a-postgresql-database)