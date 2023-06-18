# How do I use autoincrement ID in SQLite?
// plain

SQLite supports the use of an autoincrement ID, which is an automatically generated number that can be used to identify a row. To use autoincrement ID in SQLite, you need to define a column with the type INTEGER PRIMARY KEY. This column will be used to store the autoincrement ID.

For example, the following code creates a table with an autoincrement ID using the INTEGER PRIMARY KEY column:

```
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
```

When inserting new rows into the table, you can omit the autoincrement ID column from the INSERT statement. The value for the autoincrement ID will be generated automatically.

For example, the following code inserts a new row into the contacts table and the value for the autoincrement ID will be generated automatically:

```
INSERT INTO contacts (name, age) VALUES ('John Doe', 30);
```

The generated autoincrement ID can be accessed using the [last_insert_rowid()](https://www.sqlite.org/lang_corefunc.html#last_insert_rowid) function.

For example, the following code retrieves the autoincrement ID for the newly inserted row:

```
SELECT last_insert_rowid();
```

## Output example


```
1
```

- `CREATE TABLE` statement is used to create a table with an autoincrement ID using the INTEGER PRIMARY KEY column.
- `INSERT INTO` statement is used to insert a new row into the table. The autoincrement ID column can be omitted from the statement.
- `last_insert_rowid()` function is used to retrieve the autoincrement ID for the newly inserted row.

onelinerhub: [How do I use autoincrement ID in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-autoincrement-id-in-sqlite)