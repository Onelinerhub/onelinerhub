# How do I use the SQLite bool type?
// plain

The SQLite bool type is a storage class used to store either a 0 (false) or 1 (true). It is used to store boolean values in an SQLite database.

## Example code

```
CREATE TABLE test (
  id INTEGER PRIMARY KEY,
  is_active BOOL
);

INSERT INTO test (is_active) VALUES (true);

SELECT * FROM test;
```
## Output example

```
id  | is_active
----+-----------
 1  | 1
```

1. `CREATE TABLE`: This statement creates a table called `test` with two columns: `id` and `is_active`.
2. `INTEGER PRIMARY KEY`: This specifies that the `id` column is an integer and is the primary key of the table.
3. `BOOL`: This specifies that the `is_active` column is of type bool.
4. `INSERT INTO`: This statement inserts a value of `true` into the `is_active` column of the `test` table.
5. `SELECT *`: This statement retrieves all the data from the `test` table.

## Helpful links
- [SQLite Documentation](https://sqlite.org/docs.html)
- [SQLite Data Types](https://www.sqlitetutorial.net/sqlite-data-types/)

onelinerhub: [How do I use the SQLite bool type?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-bool-type)