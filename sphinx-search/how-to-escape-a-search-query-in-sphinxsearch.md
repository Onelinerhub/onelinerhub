# How to escape a search query in SphinxSearch?
// plain

SphinxSearch supports escaping special characters in search queries using backslash (`\`). For example, if you want to search for a phrase containing a special character, such as `+`, you can escape it using a backslash:

```
SELECT * FROM table WHERE MATCH('\+')
```

The output of the above query will be all the records containing the `+` character.

The following list contains the special characters that need to be escaped in SphinxSearch:

- `+`: Plus sign
- `-`: Minus sign
- `!`: Exclamation mark
- `(`: Left parenthesis
- `)`: Right parenthesis
- `{`: Left curly brace
- `}`: Right curly brace
- `[`: Left square bracket
- `]`: Right square bracket
- `^`: Caret
- `"`: Double quote
- `~`: Tilde
- `*`: Asterisk
- `?`: Question mark
- `:`: Colon

For more information, please refer to the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html#syntax-escaping).

onelinerhub: [How to escape a search query in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-escape-a-search-query-in-sphinxsearch)