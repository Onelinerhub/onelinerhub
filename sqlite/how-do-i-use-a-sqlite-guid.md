# How do I use a SQLite GUID?
// plain

A GUID (Globally Unique Identifier) is a 128-bit number used to uniquely identify records in a SQLite database. To use a GUID in SQLite, you must use the `UUID` function. This function takes no parameters and returns a unique GUID.

## Example code

```
SELECT UUID();
```

Example output:
```
2f7f3050-4a50-4f9e-9a9c-5e2b8d6f7c3f
```

The code above will generate a new GUID each time it is called. You can use this GUID to identify a record in a table. For example, to create a new record with a GUID in a table named `users`:

```
INSERT INTO users (id, name) VALUES (UUID(), 'John Doe');
```

The code above will insert a new row into the `users` table with a unique GUID as the `id` and `John Doe` as the `name`.

## Code explanation

- `SELECT UUID();`: This statement selects the UUID() function, which generates a new GUID.
- `INSERT INTO users (id, name) VALUES (UUID(), 'John Doe');`: This statement inserts a new row into the `users` table with a unique GUID as the `id` and `John Doe` as the `name`.


## Helpful links
- https://www.sqlite.org/lang_corefunc.html#uuid
- https://en.wikipedia.org/wiki/Universally_unique_identifier

onelinerhub: [How do I use a SQLite GUID?](https://onelinerhub.com/sqlite/how-do-i-use-a-sqlite-guid)