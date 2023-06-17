# How can I use PostgreSQL JSON functions?
// plain

PostgreSQL JSON functions can be used to manipulate and query JSON data.

## Example

```
SELECT row_to_json(t)
FROM (SELECT 'John' as name, 'Doe' as surname) t;

```
## Output example

```
{"name":"John","surname":"Doe"}
```

The code above uses the `row_to_json` function to create a JSON object from a row of data.

The `json_array_length` function can be used to find the length of a JSON array.

## Example

```
SELECT json_array_length('[1, 2, 3]');
```

## Output example

```
3
```

The `json_extract_path` function can be used to extract a value from a JSON object.

## Example

```
SELECT json_extract_path('{"name":"John","surname":"Doe"}', 'name');
```

## Output example

```
John
```

Other PostgreSQL JSON functions include `json_object`, `json_array`, `json_build_object`, `json_build_array`, `json_object_keys`, `json_populate_record`, `json_populate_recordset`, `json_each`, and `json_array_elements`.

## Helpful links

- [PostgreSQL Documentation - JSON Functions and Operators](https://www.postgresql.org/docs/current/functions-json.html)
- [PostgreSQL Tutorial - JSON Functions](https://www.postgresqltutorial.com/postgresql-json/)

onelinerhub: [How can I use PostgreSQL JSON functions?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-json-functions)