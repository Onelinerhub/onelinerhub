# How do I use the SQLite SUBSTRING function?
// plain

The SQLite SUBSTRING function allows you to extract a substring from a string. The syntax for the SUBSTRING function is as follows: `SUBSTRING(string, start, length)`.

For example, if you had a string `'Hello World'` and wanted to extract the substring `'Hello'`, you could use the following code:

```
SELECT SUBSTRING('Hello World', 1, 5);
```

This would return the following output:

```
Hello
```

The code is composed of the following parts:

1. `SELECT`: This is an SQLite command that tells the database to return the result of the operation.
2. `SUBSTRING(string, start, length)`: This is the SUBSTRING function, which takes three arguments:
    - `string`: The string from which you want to extract a substring.
    - `start`: The starting index of the substring, where the index of the first character is 1.
    - `length`: The length of the substring.

For more information on the SUBSTRING function, see [this page](https://www.sqlitetutorial.net/sqlite-substring/).

onelinerhub: [How do I use the SQLite SUBSTRING function?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-substring-function)