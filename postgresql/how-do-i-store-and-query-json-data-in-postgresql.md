# How do I store and query JSON data in PostgreSQL?
// plain

PostgreSQL supports the storage of JSON data in its native JSON data type. This allows you to store and query JSON data directly in the database.

## Example code

```
CREATE TABLE json_data (
  id serial PRIMARY KEY,
  data json
);

INSERT INTO json_data (data)
VALUES
  ('{"name": "John Doe", "age": 32}');

SELECT * FROM json_data;
```

## Output example

```
 id |               data
----+----------------------------------
  1 | {"name": "John Doe", "age": 32}
```

## Code explanation

- `CREATE TABLE json_data (id serial PRIMARY KEY, data json)` - Creates a table with the columns `id` and `data` where `data` is of type `json`.
- `INSERT INTO json_data (data) VALUES ('{"name": "John Doe", "age": 32}')` - Inserts a JSON object into the `data` column.
- `SELECT * FROM json_data` - Retrieves all rows from the `json_data` table.

## Helpful links
- [PostgreSQL Documentation: JSON Types](https://www.postgresql.org/docs/9.5/datatype-json.html)
- [PostgreSQL Documentation: JSON Functions and Operators](https://www.postgresql.org/docs/9.5/functions-json.html)

onelinerhub: [How do I store and query JSON data in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-store-and-query-json-data-in-postgresql)