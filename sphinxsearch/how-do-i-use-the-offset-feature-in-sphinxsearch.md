# How do I use the offset feature in SphinxSearch?
// plain

The `offset` feature in SphinxSearch allows you to specify the starting point for a query result set. This is useful for paginating query results.

For example:

```
SELECT * FROM index_name WHERE MATCH('@some_attribute some_query') LIMIT 0, 10 OPTION offset = 10;
```

This will return the second page of results from the query `@some_attribute some_query`, with the first page of results starting at the 11th result.

The parts of the example code are:

1. `SELECT * FROM index_name` - This specifies which index to search.
2. `WHERE MATCH('@some_attribute some_query')` - This specifies the query to search for.
3. `LIMIT 0, 10` - This specifies the number of results to return, starting at the 0th result.
4. `OPTION offset = 10` - This specifies the starting point for the query results, in this case the 11th result.

For more information, see the [SphinxSearch documentation](http://sphinxsearch.com/docs/2.2.11/conf-offset.html).

onelinerhub: [How do I use the offset feature in SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-use-the-offset-feature-in-sphinxsearch)