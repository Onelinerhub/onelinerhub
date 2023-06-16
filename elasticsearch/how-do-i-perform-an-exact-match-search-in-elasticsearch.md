# How do I perform an exact match search in Elasticsearch?
// plain

To perform an exact match search in Elasticsearch, you can use the `term` query. This query will match documents that have exact terms specified in the query.

For example, if you have a field `title` with value `The quick brown fox`, the following query will match the document:

```
GET /_search
{
  "query": {
    "term": {
      "title": {
        "value": "The quick brown fox"
      }
    }
  }
}
```

The output will be the document:

```
{
  "_index": "my_index",
  "_type": "_doc",
  "_id": "1",
  "_score": 1,
  "_source": {
    "title": "The quick brown fox"
  }
}
```

The `term` query consists of the following parts:

* `query`: The query type, in this case `term`
* `title`: The field to search in
* `value`: The exact value to search for

For more information, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html).

onelinerhub: [How do I perform an exact match search in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-perform-an-exact-match-search-in-elasticsearch)