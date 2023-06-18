# characters

How do I use escape characters in SphinxSearch?
// plain

In SphinxSearch, escape characters are used to represent special characters in search queries. This is done by prepending a backslash (\) to the special character. For example, the following query will search for the phrase "test phrase":

```
SELECT * FROM table WHERE MATCH('test\ phrase')
```

The backslash is used to escape the space character, so that SphinxSearch knows to search for the phrase instead of two separate words.

Here is a list of some common escape characters and their usage:

* \\\\ - Escape a single backslash
* \\+ - Escape a plus sign
* \\- - Escape a minus sign
* \\! - Escape an exclamation mark
* \\( - Escape an opening parenthesis
* \\) - Escape a closing parenthesis
* \\: - Escape a colon
* \\^ - Escape a caret
* \\[ - Escape an opening bracket
* \\] - Escape a closing bracket
* \\{ - Escape an opening brace
* \\} - Escape a closing brace
* \\~ - Escape a tilde

For more information about using escape characters in SphinxSearch, please refer to the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html#escaping-special-characters).

onelinerhub: [characters

How do I use escape characters in SphinxSearch?](https://onelinerhub.com/sphinxsearch/characters--how-do-i-use-escape-characters-in-sphinxsearch)