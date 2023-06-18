# How do I store a timestamp in an SQLite database?
// plain

Storing a timestamp in an SQLite database is done by using the `DATETIME` data type. This type is used to store date and time values in the format `YYYY-MM-DD HH:MM:SS`. An example of how to store a timestamp in an SQLite database is shown below:

```
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME NOT NULL
);

INSERT INTO my_table (timestamp) VALUES (datetime('now'));
```

The code above will create a table named `my_table` with an `id` integer primary key and a `timestamp` column of type `DATETIME`. The `INSERT` statement will add a row to the table with the current timestamp.

Parts of the code:
- `CREATE TABLE`: This statement creates a new table in the database.
- `IF NOT EXISTS`: This clause ensures that the table is only created if it does not already exist.
- `DATETIME`: This is the data type used to store the timestamp.
- `INSERT INTO`: This statement adds a row to the database table.
- `datetime('now')`: This is a function that returns the current timestamp.

## Helpful links
- [SQLite Data Types](https://www.sqlite.org/datatype3.html)
- [SQLite Insert](https://www.sqlite.org/lang_insert.html)
- [SQLite Date and Time Functions](https://www.sqlite.org/lang_datefunc.html)

onelinerhub: [How do I store a timestamp in an SQLite database?](https://onelinerhub.com/sqlite/how-do-i-store-a-timestamp-in-an-sqlite-database)