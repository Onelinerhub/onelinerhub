# How can I use an upsert statement to update data in a SQLite database?
// plain

An upsert statement can be used to update data in a SQLite database. It is a combination of the words "update" and "insert" and is a convenient way to update or insert data into a table.

The syntax for an upsert statement in SQLite is as follows:

```
INSERT INTO table_name (column1, column2, ...)
    VALUES (value1, value2, ...)
    ON CONFLICT (column1) DO
    UPDATE SET column2 = value2, column3 = value3, ...;
```

In the above statement, `table_name` is the name of the table where the data will be updated or inserted. `column1`, `column2`, etc. are the columns in the table that will be affected. `value1`, `value2`, etc. are the values that will be inserted or updated.

For example, if we wanted to update the `name` column of the `users` table with the value `John`, we could use the following statement:

```
INSERT INTO users (name) VALUES ('John')
    ON CONFLICT (name) DO
    UPDATE SET name = 'John';
```

The output of this statement will be the number of rows affected, which in this case would be 1.

## Helpful links

- [SQLite Upsert Syntax](https://www.sqlitetutorial.net/sqlite-upsert/)
- [SQLite Insert or Update (Upsert)](https://www.tutorialspoint.com/sqlite/sqlite_insert_or_update.htm)

onelinerhub: [How can I use an upsert statement to update data in a SQLite database?](https://onelinerhub.com/sqlite/how-can-i-use-an-upsert-statement-to-update-data-in-a-sqlite-database)