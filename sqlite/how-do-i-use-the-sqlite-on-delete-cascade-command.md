# How do I use the SQLite on delete cascade command?
// plain

The SQLite `ON DELETE CASCADE` command allows a user to delete related records from other tables when the record in the parent table is deleted. This command is useful for maintaining referential integrity in a database.

## Example code

```
CREATE TABLE IF NOT EXISTS parent_table (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE IF NOT EXISTS child_table (
  id INTEGER PRIMARY KEY,
  parent_id INTEGER,
  FOREIGN KEY(parent_id) REFERENCES parent_table(id) ON DELETE CASCADE
);
```

When a record in the parent table is deleted, the corresponding records in the child table will also be deleted.

## Code explanation

- `CREATE TABLE`: creates a new table in the database
- `INTEGER PRIMARY KEY`: defines the primary key for the table, which is used to uniquely identify each record
- `FOREIGN KEY`: defines a foreign key, which is used to reference a record in another table
- `REFERENCES`: specifies the table and column that the foreign key references
- `ON DELETE CASCADE`: specifies that the related records in the child table should be deleted when the record in the parent table is deleted

## Helpful links
- [SQLite Foreign Key Support](https://www.sqlite.org/foreignkeys.html)
- [SQLite ON DELETE CASCADE](https://www.sqlitetutorial.net/sqlite-on-delete-cascade/)

onelinerhub: [How do I use the SQLite on delete cascade command?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-on-delete-cascade-command)