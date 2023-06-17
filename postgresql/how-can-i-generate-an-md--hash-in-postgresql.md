# How can I generate an MD5 hash in PostgreSQL?
// plain

PostgreSQL provides a built-in function for generating MD5 hashes called `md5()`. It takes a single argument, which can be either a text string or a bytea data type. To generate an MD5 hash of a text string, use the following syntax:

```SQL
SELECT md5('MyTextString');
```

## Output example

```
f2d6c7f6f1b556bb9aefef8c1e5cf149
```

The syntax for generating an MD5 hash from a bytea data type is as follows:

```SQL
SELECT md5(BYTEA_COLUMN);
```

The `md5()` function returns the generated MD5 hash as a 32-character hexadecimal string.

## Code explanation


- `SELECT md5(`: This is the SQL command used to generate an MD5 hash.
- `'MyTextString'`: This is the argument passed to the `md5()` function, which in this case is a text string.
- `BYTEA_COLUMN`: This is the argument passed to the `md5()` function, which in this case is a bytea data type.

## Helpful links

- [PostgreSQL Documentation: MD5](https://www.postgresql.org/docs/9.6/functions-string.html#FUNCTIONS-STRING-SQL-MD5)

onelinerhub: [How can I generate an MD5 hash in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-generate-an-md--hash-in-postgresql)