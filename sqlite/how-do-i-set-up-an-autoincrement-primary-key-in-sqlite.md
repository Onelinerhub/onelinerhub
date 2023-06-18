# How do I set up an autoincrement primary key in SQLite?
// plain

To set up an autoincrement primary key in SQLite, you need to use the `INTEGER PRIMARY KEY` column type. This column type will automatically assign an integer value for each new row, starting from 1 and incrementing by 1 for each new row.

For example, to create a table with an autoincrement primary key, you could use the following SQL statement:

```sql
CREATE TABLE test (
    id INTEGER PRIMARY KEY,
    name TEXT
);
```

This will create a table with two columns: `id` and `name`. The `id` column will be an integer primary key that autoincrements.

Parts of the code:

* `CREATE TABLE test` - Creates a new table named `test`.
* `id INTEGER PRIMARY KEY` - Creates a column named `id` with type `INTEGER PRIMARY KEY`. This will be the autoincrement primary key.
* `name TEXT` - Creates a column named `name` with type `TEXT`.

## Helpful links

* [SQLite Documentation - INTEGER PRIMARY KEY](https://sqlite.org/autoinc.html)

onelinerhub: [How do I set up an autoincrement primary key in SQLite?](https://onelinerhub.com/sqlite/how-do-i-set-up-an-autoincrement-primary-key-in-sqlite)