# How do I retrieve the last insert ID in SQLite?
// plain

The `last_insert_rowid()` function can be used to retrieve the last insert ID in SQLite. This function is used to retrieve the rowid of the last row insert from the database connection which invoked the function.

## Example code

```
INSERT INTO contacts (firstname, lastname) VALUES ('John', 'Doe');
SELECT last_insert_rowid();
```

## Output example

```
1
```

The code above inserts a new row into the `contacts` table and then retrieves the rowid of the last row insert. In this case, the rowid is `1`.

## Code explanation

- `INSERT INTO`: this is a SQL statement used to insert a row into a table
- `contacts`: this is the name of the table
- `firstname` and `lastname`: these are the column names of the table
- `VALUES`: this is a keyword used to specify the values to be inserted
- `John` and `Doe`: these are the values to be inserted
- `SELECT`: this is a SQL statement used to select data from a table
- `last_insert_rowid()`: this is the function used to retrieve the last insert ID

## Helpful links
- [SQLite Documentation - last_insert_rowid()](https://www.sqlite.org/lang_corefunc.html#last_insert_rowid)

onelinerhub: [How do I retrieve the last insert ID in SQLite?](https://onelinerhub.com/sqlite/how-do-i-retrieve-the-last-insert-id-in-sqlite)