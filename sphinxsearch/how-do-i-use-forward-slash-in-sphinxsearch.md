# How do I use forward slash in SphinxSearch?
// plain

The forward slash (`/`) is used to denote a regular expression in the SphinxSearch query syntax. A regular expression is a sequence of characters that define a search pattern.

For example, the following query searches for the word `cat` or `dog`:

```
SELECT * FROM index WHERE MATCH('cat / dog')
```

The code above can be broken down into the following parts:

- `SELECT * FROM index`: This part of the code specifies which index to search in.
- `WHERE MATCH('cat / dog')`: This part of the code specifies the search query. The forward slash (`/`) is used to denote a regular expression, which in this case is `cat` or `dog`.

For more information on regular expressions in SphinxSearch, please refer to the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html#sphinxql-syntax-queries).

onelinerhub: [How do I use forward slash in SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-use-forward-slash-in-sphinxsearch)