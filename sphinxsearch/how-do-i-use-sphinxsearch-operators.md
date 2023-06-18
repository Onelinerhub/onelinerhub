# How do I use SphinxSearch operators?
// plain

SphinxSearch is a powerful open source search engine that is used to index and search data stored in a variety of formats. It supports a wide range of operators that can be used to refine searches and make them more accurate.

The following example shows how to use the `AND` operator to search for documents containing both the words "cat" and "dog":

```
SELECT * FROM documents WHERE MATCH('cat AND dog')
```

The following operators are supported by SphinxSearch:

* `AND`: returns documents that contain both of the words specified.
* `OR`: returns documents that contain either of the words specified.
* `NOT`: returns documents that contain the first word but not the second.
* `NEAR`: returns documents that contain both words within a certain distance of each other.
* `SENTENCE`: returns documents that contain the words in the specified order.
* `PROXIMITY`: returns documents that contain both words within a certain distance of each other, regardless of order.

For more information about SphinxSearch operators, please refer to the [official documentation](http://sphinxsearch.com/docs/current.html#sphinxql-syntax-queries).

onelinerhub: [How do I use SphinxSearch operators?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-operators)