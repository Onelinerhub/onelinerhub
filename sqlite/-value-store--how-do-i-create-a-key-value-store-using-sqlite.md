# -value store

How do I create a key-value store using SQLite?
// plain

A key-value store is a database which stores data as a collection of key-value pairs. SQLite is a lightweight, self-contained database engine that can be used to create a key-value store.

To create a key-value store using SQLite, you must first create a table with two columns - a key column and a value column. The following example creates a table called `kv_store` with two columns - `key` and `value` - of type `TEXT`:

```
CREATE TABLE kv_store (
    key TEXT,
    value TEXT
);
```

You can then insert new key-value pairs into the table using the `INSERT` statement. The following example inserts a key-value pair with a key of `name` and a value of `John`:

```
INSERT INTO kv_store (key, value) VALUES ('name', 'John');
```

You can then retrieve the value for a given key using the `SELECT` statement. The following example retrieves the value for the key `name`:

```
SELECT value FROM kv_store WHERE key = 'name';
```

The output of this statement is:

```
John
```

To summarize, to create a key-value store using SQLite, you must:

1. Create a table with two columns - a key column and a value column.
2. Insert new key-value pairs into the table using the `INSERT` statement.
3. Retrieve the value for a given key using the `SELECT` statement.

## Helpful links

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [-value store

How do I create a key-value store using SQLite?](https://onelinerhub.com/sqlite/-value-store--how-do-i-create-a-key-value-store-using-sqlite)