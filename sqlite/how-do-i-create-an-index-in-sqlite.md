# How do I create an index in SQLite?
// plain

To create an index in SQLite, you can use the following SQL statement:

```
CREATE INDEX index_name ON table_name(column_name);
```

For example, to create an index called `index_name` on the `table_name` table, based on the `column_name` column:

```
CREATE INDEX index_name ON table_name(column_name);
```

The output of this statement will be `index_name` if the index is successfully created.

The parts of the code are:
- `CREATE INDEX` - this is the command to create an index
- `index_name` - this is the name of the index being created
- `ON table_name` - this is the name of the table on which the index is being created
- `(column_name)` - this is the name of the column on which the index is being created

## Helpful links
- [SQLite Documentation - CREATE INDEX Statement](https://www.sqlite.org/lang_createindex.html)
- [SQLite Tutorial - Create Index](https://www.sqlitetutorial.net/sqlite-index/)

onelinerhub: [How do I create an index in SQLite?](https://onelinerhub.com/sqlite/how-do-i-create-an-index-in-sqlite)