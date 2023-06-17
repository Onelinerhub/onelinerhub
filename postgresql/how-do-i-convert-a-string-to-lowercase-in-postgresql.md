# How do I convert a string to lowercase in PostgreSQL?
// plain

To convert a string to lowercase in PostgreSQL, you can use the `LOWER` function. This function takes a string as its argument and returns the same string in all lowercase letters.

For example, the following code block:
```
SELECT LOWER('STRING');
```
will return the following output:
```
string
```

The `LOWER` function can be used in a variety of contexts, such as in a `SELECT` clause, in a `WHERE` clause, and in a `GROUP BY` clause.

The syntax for the `LOWER` function is as follows:

`LOWER(string)`

Where `string` is the string to be converted to lowercase.

Here are some useful links for more information on the `LOWER` function:

- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-SQL)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/postgresql-lower-function/)

onelinerhub: [How do I convert a string to lowercase in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-convert-a-string-to-lowercase-in-postgresql)