# How to use filters in SphinxSearch?
// plain

Filters in SphinxSearch are used to limit the search results to a specific set of values.

## Example

```
SELECT * FROM table WHERE MATCH('keyword') AND filter=value
```

This will return all rows from the table that match the keyword and have the filter set to the specified value.

## Code explanation

- SELECT * FROM table: This is the SQL query used to select all rows from the table.
- MATCH('keyword'): This is the SphinxSearch query used to search for the specified keyword.
- AND filter=value: This is the filter used to limit the search results to a specific set of values.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Filters](http://sphinxsearch.com/docs/current.html#filters)

onelinerhub: [How to use filters in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-filters-in-sphinxsearch)