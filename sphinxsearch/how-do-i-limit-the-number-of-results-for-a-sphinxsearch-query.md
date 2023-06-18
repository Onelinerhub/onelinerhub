# How do I limit the number of results for a SphinxSearch query?
// plain

To limit the number of results for a SphinxSearch query, you can use the `LIMIT` clause. This clause takes two arguments: the offset and the number of results. For example:

```
SELECT * FROM index_name WHERE MATCH('@column_name value') LIMIT 0, 10;
```

This query will return the first 10 results that match the given criteria.

The parts of this query are:

* `SELECT * FROM index_name`: This is the command to select all the fields from the given index.
* `WHERE MATCH('@column_name value')`: This is the criteria for the search.
* `LIMIT 0, 10`: This is the clause to limit the number of results. The first argument is the offset, and the second is the number of results.

For more information, please see the [Sphinx Documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I limit the number of results for a SphinxSearch query?](https://onelinerhub.com/sphinxsearch/how-do-i-limit-the-number-of-results-for-a-sphinxsearch-query)