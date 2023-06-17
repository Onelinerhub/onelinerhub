# How do I use regexp_replace in PostgreSQL?
// plain

`regexp_replace` is a function in PostgreSQL that allows you to replace a substring in a string using regular expressions. It takes three arguments: the string, the pattern to match, and the replacement string.

## Example


```
SELECT regexp_replace('Hello World', 'World', 'PostgreSQL');
```

## Output example


`Hello PostgreSQL`

The code above takes the string "Hello World" and replaces the substring "World" with the string "PostgreSQL".

The parts of the code are:
- `regexp_replace`: the function that performs the replacement
- `'Hello World'`: the string that contains the substring that needs to be replaced
- `'World'`: the substring that needs to be replaced
- `'PostgreSQL'`: the string that will be used to replace the substring

## Helpful links
- [PostgreSQL Documentation - regexp_replace](https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-SQL)

onelinerhub: [How do I use regexp_replace in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-use-regexp-replace-in-postgresql)