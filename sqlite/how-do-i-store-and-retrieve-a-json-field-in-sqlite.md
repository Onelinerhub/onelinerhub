# How do I store and retrieve a JSON field in SQLite?
// plain

Storing and retrieving a JSON field in SQLite can be done using the `json1` extension. To store a JSON field, you can use the `json_insert` function. For example:

```
sqlite> INSERT INTO test_table (json_data) VALUES (json_insert('{"name": "John Doe", "age": 25}'));
```

To retrieve a JSON field, you can use the `json_extract` function. For example:

```
sqlite> SELECT json_extract(json_data, '$.name') FROM test_table;
John Doe
```

## Code explanation

- `json_insert`: a function used to store a JSON field in a SQLite database.
- `json_extract`: a function used to retrieve a JSON field from a SQLite database.

## Helpful links
- [SQLite json1 Extension](https://www.sqlite.org/json1.html)
- [Storing and Retrieving JSON in SQLite](https://www.sqlitetutorial.net/sqlite-json/)

onelinerhub: [How do I store and retrieve a JSON field in SQLite?](https://onelinerhub.com/sqlite/how-do-i-store-and-retrieve-a-json-field-in-sqlite)