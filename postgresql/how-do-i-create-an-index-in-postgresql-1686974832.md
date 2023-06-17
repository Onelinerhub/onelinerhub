# How do I create an index in PostgreSQL?
// plain

Creating an index in PostgreSQL is a simple process. First, you must specify the table and column you wish to create the index on:

```
CREATE INDEX index_name ON table_name (column_name);
```

This will create an index on the specified table and column. You can also specify multiple columns, if desired:

```
CREATE INDEX index_name ON table_name (column_name1, column_name2);
```

If you wish to create a unique index, you can specify the `UNIQUE` keyword:

```
CREATE UNIQUE INDEX index_name ON table_name (column_name);
```

You can also specify a name for the index:

```
CREATE INDEX index_name ON table_name (column_name) USING btree (index_name);
```

This will create an index on the specified table and column with the specified name.

You can also specify sorting order:

```
CREATE INDEX index_name ON table_name (column_name) USING btree (index_name) ORDER BY column_name;
```

This will create an index on the specified table and column with the specified name and sorting order.

## Helpful links
- [PostgreSQL Documentation - CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html)
- [PostgreSQL Tutorial - Indexes](https://www.postgresqltutorial.com/postgresql-indexes/)

onelinerhub: [How do I create an index in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-an-index-in-postgresql-1686974832)