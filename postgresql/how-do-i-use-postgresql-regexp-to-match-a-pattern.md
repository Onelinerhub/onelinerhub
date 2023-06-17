# How do I use PostgreSQL regexp to match a pattern?
// plain

PostgreSQL provides the `regexp_matches` function to match a pattern. This function returns all matched parts of a string.

## Example


```
SELECT regexp_matches('Hello World', '\w+ \w+', 'g');
```

## Output example


```
{Hello,World}
```

The code above uses `regexp_matches` to search for two words in a string.

Parts of the code:
- `SELECT regexp_matches` - this is the function used to match a pattern
- `('Hello World', '\w+ \w+', 'g')` - this is the pattern to be matched. `\w+ \w+` means one or more word characters followed by a space followed by one or more word characters. The `g` flag stands for global and means that the pattern should be matched multiple times.

## Helpful links
- [PostgreSQL Documentation - Regular Expressions](https://www.postgresql.org/docs/9.1/functions-matching.html#FUNCTIONS-POSIX-REGEXP)
- [Regular Expressions Cheat Sheet](https://www.debuggex.com/cheatsheet/regex/pcre)

onelinerhub: [How do I use PostgreSQL regexp to match a pattern?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-regexp-to-match-a-pattern)