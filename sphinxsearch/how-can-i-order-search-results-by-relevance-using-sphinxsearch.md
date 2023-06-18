# How can I order search results by relevance using SphinxSearch?
// plain

To order search results by relevance using SphinxSearch, you can use the `SET` clause in the query. For example, the following query orders the results by relevance, using the `weight` field:

```sql
SELECT * FROM index_name
WHERE MATCH('keywords')
SET weight DESC;
```

The `SET` clause is used to sort the results using one or more fields. In the above example, the `weight` field is used to sort the results. The `DESC` keyword indicates that the results should be sorted in descending order.

The `weight` field is used to indicate the relevance of the results. Generally, the higher the `weight` value, the more relevant the result.

The following list explains the parts of the query:

* `SELECT * FROM index_name` – This part of the query specifies the index to be used for the search.
* `WHERE MATCH('keywords')` – This part of the query specifies the keywords to search for.
* `SET weight DESC` – This part of the query specifies the field to sort the results by (`weight`) and the order (`DESC`).

For more information, see the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How can I order search results by relevance using SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-can-i-order-search-results-by-relevance-using-sphinxsearch)