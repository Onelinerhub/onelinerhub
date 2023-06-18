# How do I use Sphinx Search to find exact matches?
// plain

Sphinx Search is a powerful open-source full-text search engine that can be used to find exact matches. To do this, you need to use the SphinxQL query language.

For example, to find an exact match for the word "cat" in a table called "animals" you can use the following query:

```
SELECT * FROM animals WHERE MATCH('cat')
```

This query will return all records from the "animals" table that contain the exact word "cat".

## Code explanation


- `SELECT *`: This is the statement used to select all records from a table.
- `FROM animals`: This is the statement used to specify the table from which records should be selected.
- `WHERE MATCH('cat')`: This is the statement used to specify a search term. In this case, it is used to search for the exact word "cat".

For more information about Sphinx Search, please refer to the [official documentation](http://sphinxsearch.com/docs/).

onelinerhub: [How do I use Sphinx Search to find exact matches?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-search-to-find-exact-matches)