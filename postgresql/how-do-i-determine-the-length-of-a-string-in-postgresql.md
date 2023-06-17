# How do I determine the length of a string in PostgreSQL?
// plain

To determine the length of a string in PostgreSQL, you can use the `LENGTH()` function. This function takes a string as an argument and returns the length of the string.

For example, the following code block returns the length of the string `Hello World`:

```
SELECT LENGTH('Hello World');
```

## Output example

```
11
```

The code consists of two parts:
1. `SELECT`: This statement is used to select data from a database.
2. `LENGTH('Hello World')`: This function takes a string as an argument and returns the length of the string.

For more information, please refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/9.3/functions-string.html).

onelinerhub: [How do I determine the length of a string in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-determine-the-length-of-a-string-in-postgresql)