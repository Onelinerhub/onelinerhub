# How can I store JSON data in a SQLite column?
// plain

SQLite is a lightweight database that can be used to store JSON data. To store JSON data in a SQLite column, you can use the `JSON1` extension. This extension provides functions for encoding and decoding JSON data, as well as functions for manipulating and querying JSON data.

The following code block uses the `json_extract()` function to store JSON data in a SQLite column:

```
CREATE TABLE json_data (
  id INTEGER PRIMARY KEY,
  json_column TEXT
);

INSERT INTO json_data (json_column) VALUES (
  json_extract('{"name":"John","age":30}', '$.name')
);

SELECT * FROM json_data;
```

## Output example

```
id	json_column
1	John
```

The code above:
1. Creates a table named `json_data` with an `id` column and a `json_column` column.
2. Inserts a JSON string into the `json_column` column.
3. Selects all data from the `json_data` table.

## Helpful links
1. [SQLite JSON1 Extension](https://www.sqlite.org/json1.html)
2. [Using JSON in SQLite](https://www.sqlitetutorial.net/sqlite-json/)

onelinerhub: [How can I store JSON data in a SQLite column?](https://onelinerhub.com/sqlite/how-can-i-store-json-data-in-a-sqlite-column)