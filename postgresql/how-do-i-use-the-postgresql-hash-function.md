# How do I use the PostgreSQL hash function?
// plain

The PostgreSQL `HASH` function is a cryptographic hash function used to generate a hash value from a string of text. It is used to generate a unique value from a given string of data which can be used to identify a record or verify data integrity.

## Example


```
SELECT HASH('Hello World');

## Output example


7e9d4a6bcef9f9e2f3a9d9a3f6f6f1f2
```

The `HASH` function takes a single argument, which is the string of text to be hashed. In this example, the string 'Hello World' is hashed. The output is a 32 character hexadecimal string.

The `HASH` function is also available in other languages, such as C, Java, and Python.

Parts of the code:

- `SELECT`: The keyword used to select data from a table.
- `HASH`: The PostgreSQL function used to generate a hash value from a string of text.
- `'Hello World'`: The argument passed to the `HASH` function, which is the string of text to be hashed.

## Helpful links

- [PostgreSQL Documentation: HASH](https://www.postgresql.org/docs/9.6/functions-string.html#FUNCTIONS-STRING-OTHER)
- [PostgreSQL Hashing Tutorial](https://www.guru99.com/postgresql-hashing-tutorial.html)

onelinerhub: [How do I use the PostgreSQL hash function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-hash-function)