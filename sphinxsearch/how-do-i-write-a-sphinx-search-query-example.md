# How do I write a Sphinx search query example?
// plain

Writing Sphinx search query is easy and straightforward. Here is an example of a Sphinx search query:

```
SELECT * FROM index_name WHERE MATCH('keyword')
```

This query will search the `index_name` index for documents containing the keyword `keyword`.

## Code explanation


- `SELECT` - This is the command used to select the fields you want to return from the database.
- `*` - This is a wildcard character that will return all fields from the documents in the index.
- `FROM` - This is the command used to specify the index you want to search.
- `index_name` - This is the name of the index you want to search.
- `WHERE` - This is the command used to specify the search criteria.
- `MATCH` - This is the command used to specify the keyword you want to search for.
- `keyword` - This is the keyword you want to search for.

Here are some helpful links for more information about Sphinx search queries:

- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [Sphinx Search Query Syntax](http://sphinxsearch.com/docs/current.html#query-syntax)
- [Sphinx Search Examples](http://sphinxsearch.com/docs/current.html#query-examples)

onelinerhub: [How do I write a Sphinx search query example?](https://onelinerhub.com/sphinxsearch/how-do-i-write-a-sphinx-search-query-example)