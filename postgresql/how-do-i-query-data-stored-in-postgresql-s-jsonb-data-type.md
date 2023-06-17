# How do I query data stored in PostgreSQL's JSONB data type?
// plain

PostgreSQL's JSONB data type is a binary representation of JSON that allows for fast read/write access and indexing. To query data stored in JSONB, the `->` and `->>` operators can be used.

The `->` operator will return a JSON object, while the `->>` operator will return text.

For example:
```
SELECT
    my_json->'name' AS name,
    my_json->'age' AS age
FROM
    my_table;
```
This will return the `name` and `age` fields from the `my_json` JSONB column in `my_table`.

The following list explains the parts of the example query:
1. `SELECT` - begins the query and specifies which columns to return
2. `my_json->'name'` - uses the `->` operator to return the `name` field from the `my_json` column as a JSON object
3. `AS name` - assigns the result of the `->` operator to the `name` column
4. `my_json->'age'` - uses the `->` operator to return the `age` field from the `my_json` column as a JSON object
5. `AS age` - assigns the result of the `->` operator to the `age` column
6. `FROM my_table` - specifies the table to query

## Helpful links
- [PostgreSQL Documentation - JSON Types](https://www.postgresql.org/docs/9.5/datatype-json.html)
- [PostgreSQL Documentation - JSON Functions and Operators](https://www.postgresql.org/docs/9.5/functions-json.html)

onelinerhub: [How do I query data stored in PostgreSQL's JSONB data type?](https://onelinerhub.com/postgresql/how-do-i-query-data-stored-in-postgresql-s-jsonb-data-type)