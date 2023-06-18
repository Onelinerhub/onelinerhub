# store

How do I use SQLite to create a key-value store?
// plain

SQLite is a popular open source database that can be used to create a key-value store. To do this, you first need to create a table with two columns, one for the key and one for the value. For example, the following SQL statement will create a table named "my_store":

```
CREATE TABLE my_store (
    key TEXT PRIMARY KEY,
    value TEXT
);
```

Then, you can use the INSERT statement to add key-value pairs to the table. For example:

```
INSERT INTO my_store (key, value)
VALUES ('name', 'John Doe');
```

To retrieve a value, you can use the SELECT statement. For example:

```
SELECT value FROM my_store WHERE key = 'name';

# Output: John Doe
```

To update a value, you can use the UPDATE statement. For example:

```
UPDATE my_store SET value = 'Jane Doe' WHERE key = 'name';
```

To delete a value, you can use the DELETE statement. For example:

```
DELETE FROM my_store WHERE key = 'name';
```

For more information about how to use SQLite to create a key-value store, see the [SQLite Documentation](https://www.sqlite.org/lang_createtable.html).

onelinerhub: [store

How do I use SQLite to create a key-value store?](https://onelinerhub.com/sqlite/store--how-do-i-use-sqlite-to-create-a-key-value-store)