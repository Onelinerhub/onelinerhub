# How to use query_log_format in SphinxSearch?
// plain

SphinxSearch supports a query log format which can be used to log queries and their results. This can be enabled by setting the `query_log_format` option in the Sphinx configuration file.

## Example code

```
query_log_format = query_time:%T\tquery_time_total:%Tt\tquery:%q\tmatches:%m\twords:%w\tdocs:%d
```

This will log the query time, total query time, query string, number of matches, number of words, and number of documents.

## Code explanation

- `query_time`: The time taken to execute the query
- `query_time_total`: The total time taken to execute the query
- `query`: The query string
- `matches`: The number of matches found
- `words`: The number of words in the query
- `docs`: The number of documents returned

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How to use query_log_format in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-query_log_format-in-sphinxsearch)