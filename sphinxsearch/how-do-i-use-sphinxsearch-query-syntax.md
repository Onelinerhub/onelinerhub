# How do I use SphinxSearch query syntax?
// plain

SphinxSearch query syntax is used to search for specific information in a database. It is a full-text search engine written in C++ and designed to be used as a standalone search engine for websites and applications.

The syntax consists of a set of keywords, operators, and modifiers that are used to construct a query. The query is then evaluated and the results are returned.

Example query using SphinxSearch syntax:

```
SELECT * FROM table WHERE MATCH('keyword1 keyword2')
```

This query will search for documents that contain both the words "keyword1" and "keyword2".

The following operators and modifiers can be used with SphinxSearch query syntax:

* `*` - Wildcard operator.
* `~` - Proximity operator.
* `@` - Field operator.
* `( )` - Grouping operator.
* `AND`, `OR`, `NOT` - Boolean operators.

For more information about SphinxSearch query syntax, please refer to the [official documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I use SphinxSearch query syntax?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-query-syntax)