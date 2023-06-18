# How do I use different data types in SQLite?
// plain

SQLite supports a variety of data types including NULL, INTEGER, REAL, TEXT, BLOB.

```
-- Create a table with different data types
CREATE TABLE table_name (
    column_1 INTEGER,
    column_2 REAL,
    column_3 TEXT,
    column_4 BLOB
);

-- Insert a row with different data types
INSERT INTO table_name (column_1, column_2, column_3, column_4)
VALUES (1, 3.14, 'Hello SQLite', 'ABC');
```

The example code creates a table with four columns of different data types and inserts a row with different data types.

## Code explanation


* `CREATE TABLE table_name (column_1 INTEGER, column_2 REAL, column_3 TEXT, column_4 BLOB);`
    * This code creates a table named `table_name` with four columns of different data types: `column_1` of `INTEGER` type, `column_2` of `REAL` type, `column_3` of `TEXT` type and `column_4` of `BLOB` type.

* `INSERT INTO table_name (column_1, column_2, column_3, column_4) VALUES (1, 3.14, 'Hello SQLite', 'ABC');`
    * This code inserts a row into `table_name` with different data types: `column_1` is of `INTEGER` type with value `1`, `column_2` is of `REAL` type with value `3.14`, `column_3` is of `TEXT` type with value `Hello SQLite` and `column_4` is of `BLOB` type with value `ABC`.

## Helpful links
* [SQLite Data Types](https://www.sqlite.org/datatype3.html)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How do I use different data types in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-different-data-types-in-sqlite)