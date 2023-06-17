# How do I split a string in PostgreSQL?
// plain

PostgreSQL provides a built-in function to split a string into an array of substrings based on a specified delimiter. This function is called `string_to_array()`.

The syntax for the `string_to_array()` function is as follows:

```
string_to_array(string text, delimiter text)
```

## Example


```
SELECT string_to_array('1,2,3,4,5', ',');

-- Output:
{"1","2","3","4","5"}
```

The `string_to_array()` function takes two arguments:

1. `string` - The string to be split.
2. `delimiter` - The character or characters used to separate the string.

The `string_to_array()` function returns an array of substrings.

## Helpful links

- [PostgreSQL Documentation - String Functions and Operators](https://www.postgresql.org/docs/current/functions-string.html)
- [PostgreSQL Documentation - String-to-Array](https://www.postgresql.org/docs/current/functions-string-string_to_array.html)

onelinerhub: [How do I split a string in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-split-a-string-in-postgresql)