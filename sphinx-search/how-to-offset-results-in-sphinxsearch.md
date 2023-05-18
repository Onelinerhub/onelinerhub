# How to offset results in SphinxSearch?
// plain

SphinxSearch provides the ability to offset results using the `OFFSET` clause. This clause allows you to skip a certain number of results from the beginning of the result set. For example, the following query will return the second page of results (skipping the first 10 results):
```
SELECT * FROM index WHERE MATCH('test') OFFSET 10;
```
The `OFFSET` clause consists of the following parts:
- `OFFSET`: This is the keyword used to indicate that the query should skip a certain number of results.
- `10`: This is the number of results to skip.

In addition to the `OFFSET` clause, SphinxSearch also provides the `LIMIT` clause, which allows you to limit the number of results returned. For example, the following query will return the second page of results (skipping the first 10 results and limiting the result set to 10 results):
```
SELECT * FROM index WHERE MATCH('test') OFFSET 10 LIMIT 10;
```

The `LIMIT` clause consists of the following parts:
- `LIMIT`: This is the keyword used to indicate that the query should limit the number of results returned.
- `10`: This is the maximum number of results to return.

For more information about the `OFFSET` and `LIMIT` clauses, please refer to the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html#sphinxql-select).

onelinerhub: [How to offset results in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-offset-results-in-sphinxsearch)