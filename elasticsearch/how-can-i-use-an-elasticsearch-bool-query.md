# How can I use an Elasticsearch bool query?
// plain

An Elasticsearch bool query is a type of search query that allows you to combine multiple individual queries together, either as a "must" clause (all conditions must be met) or as a "should" clause (at least one condition must be met).

For example, the following query would return all documents that contain both the terms "Elasticsearch" and "bool query":

```
GET /_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "Elasticsearch" }},
        { "match": { "title": "bool query" }}
      ]
    }
  }
}
```

The output of the above query would be a list of documents that contain both the terms "Elasticsearch" and "bool query".

You can also use a "should" clause to specify that at least one of the conditions must be met. For example, the following query would return all documents that contain either the term "Elasticsearch" or the term "bool query":

```
GET /_search
{
  "query": {
    "bool": {
      "should": [
        { "match": { "title": "Elasticsearch" }},
        { "match": { "title": "bool query" }}
      ]
    }
  }
}
```

The output of the above query would be a list of documents that contain either the term "Elasticsearch" or the term "bool query".

You can also use other types of queries with bool queries, such as range queries, wildcard queries, and more. For more information about using bool queries, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html).

onelinerhub: [How can I use an Elasticsearch bool query?](https://onelinerhub.com/elasticsearch/how-can-i-use-an-elasticsearch-bool-query)