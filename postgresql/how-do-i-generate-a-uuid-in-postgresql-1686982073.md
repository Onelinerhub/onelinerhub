# How do I generate a UUID in PostgreSQL?
// plain

A UUID (Universally Unique Identifier) is a 128-bit number used to identify information in computer systems. In PostgreSQL, you can generate a UUID using the `uuid_generate_v4()` function.

## Example code

```
SELECT uuid_generate_v4();
```

Example output:
```
d1f9f02b-721a-4a0f-a2b4-2b9b7f9d2d4e
```

The code consists of the following parts:
- `SELECT`: This is the SQL command used to select data from a table.
- `uuid_generate_v4()`: This is the function used to generate a UUID in PostgreSQL.

You can also generate a UUID using other functions such as `uuid_generate_v1()`, `uuid_generate_v3()`, and `uuid_generate_v5()`.

For more information, please refer to the following links:
- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/functions-uuid.html)
- [Stack Overflow](https://stackoverflow.com/questions/111430/how-do-i-generate-a-uuid-in-postgresql)

onelinerhub: [How do I generate a UUID in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-generate-a-uuid-in-postgresql-1686982073)