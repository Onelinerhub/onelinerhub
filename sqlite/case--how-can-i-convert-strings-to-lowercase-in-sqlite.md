# case

How can I convert strings to lowercase in SQLite?
// plain

The SQLite `LOWER()` function is used to convert a string to lowercase. This function takes a single string as an argument and returns a new string that is converted to lowercase.

## Example

```
SELECT LOWER('Hello World');
```
## Output example

```
hello world
```

The code above takes the string `'Hello World'` as an argument and uses the `LOWER()` function to convert it to lowercase. The resulting string `'hello world'` is then returned.

## Code explanation

- `SELECT`: this is a SQLite command used to select data from a database table.
- `LOWER()`: this is the SQLite function used to convert a string to lowercase.
- `'Hello World'`: this is the string argument that is passed to the `LOWER()` function.

## Helpful links
- [SQLite Documentation - LOWER() Function](https://www.sqlite.org/lang_corefunc.html#lower)

onelinerhub: [case

How can I convert strings to lowercase in SQLite?](https://onelinerhub.com/sqlite/case--how-can-i-convert-strings-to-lowercase-in-sqlite)