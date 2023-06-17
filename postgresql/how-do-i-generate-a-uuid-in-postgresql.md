# How do I generate a UUID in PostgreSQL?
// plain

You can generate a UUID in PostgreSQL using the `uuid_generate_v4()` function. This function generates a version 4 UUID, which is a randomly generated UUID.

## Example

```
SELECT uuid_generate_v4();
```
## Output example

```
7c9f2a8d-6d5f-4ce3-b9f7-5e7d6f8c3d02
```

The `uuid_generate_v4()` function has the following parts:

- `uuid_generate_v4()`: The function name.
- `SELECT`: The keyword used to query the database.

More information about the `uuid_generate_v4()` function can be found in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-uuid.html).

onelinerhub: [How do I generate a UUID in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-generate-a-uuid-in-postgresql)