# How can I write a PostgreSQL query to retrieve JSON data?
// plain

A PostgreSQL query to retrieve JSON data can be written using `SELECT json_agg(t)` to aggregate the data into a single JSON object.

For example:
```
SELECT json_agg(t)
FROM (
  SELECT id, name
  FROM users
) t;
```

This will return a JSON object containing all of the users in the table:
```
[
  {
    "id": 1,
    "name": "John"
  },
  {
    "id": 2,
    "name": "Jane"
  }
]
```

The code is composed of the following parts:
- `SELECT json_agg(t)` is used to aggregate the data into a single JSON object.
- `FROM (SELECT id, name FROM users) t` is the subquery used to retrieve the data from the `users` table.
- `SELECT id, name` is the list of columns to be included in the JSON object.

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-json.html).

onelinerhub: [How can I write a PostgreSQL query to retrieve JSON data?](https://onelinerhub.com/postgresql/how-can-i-write-a-postgresql-query-to-retrieve-json-data)