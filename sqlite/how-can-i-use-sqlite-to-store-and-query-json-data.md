# How can I use SQLite to store and query JSON data?
// plain

SQLite can be used to store and query JSON data with the [JSON1 extension](https://www.sqlite.org/json1.html). The extension provides a set of SQL functions for storing and querying JSON data.

For example, the following code block uses the `json_insert()` function to insert a JSON document into a table:
```
CREATE TABLE test_table (id INTEGER PRIMARY KEY, doc JSON);
INSERT INTO test_table (doc) VALUES (json_insert('{"name": "John Doe"}'));
```

The following code block uses the `json_extract()` function to query the JSON document stored in the table:
```
SELECT json_extract(doc, '$.name') FROM test_table;
```
## Output example

```
John Doe
```

The JSON1 extension provides a range of functions for manipulating and querying JSON data, including `json_extract()`, `json_insert()`, `json_replace()`, `json_set()`, and `json_remove()`. For more information, see the [SQLite JSON1 documentation](https://www.sqlite.org/json1.html).

onelinerhub: [How can I use SQLite to store and query JSON data?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-to-store-and-query-json-data)