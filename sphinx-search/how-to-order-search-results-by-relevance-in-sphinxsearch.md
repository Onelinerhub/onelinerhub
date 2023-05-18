# How to order search results by relevance in SphinxSearch?
// plain

SphinxSearch provides a way to order search results by relevance. This can be done by using the `weight()` function.

```
SELECT * FROM index WHERE MATCH('query') ORDER BY weight() DESC;
```

The code above will return the search results ordered by relevance. The `RANK()` function will assign a relevance score to each result based on the relevance of the query to the result.

- `SELECT *`: This will select all columns from the index.
- `MATCH('query')`: This will search the index for the given query.
- `ORDER BY weight() DESC`: This will order the results by relevance in descending order.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How to order search results by relevance in SphinxSearch?
](https://onelinerhub.com/sphinx-search/how-to-order-search-results-by-relevance-in-sphinxsearch)
