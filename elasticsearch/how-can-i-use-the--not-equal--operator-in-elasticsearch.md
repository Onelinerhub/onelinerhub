# How can I use the "not equal" operator in Elasticsearch?
// plain

The "not equal" operator in Elasticsearch is used to compare two values and return documents where the values are not equal. This operator is represented by the "!=" symbol.

For example, to find documents where the "age" field is not equal to 30, the following query can be used:

```
GET /index/_search
{
  "query": {
    "bool": {
      "must_not": {
        "term": {
          "age": 30
        }
      }
    }
  }
}
```

The parts of the example query are:

* `GET /index/_search` - The request to search the index.
* `"query": { "bool": { "must_not": { "term": { "age": 30 } } } }` - The query that uses the "must_not" clause to check for documents where the "age" field is not equal to 30.

For more information, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html#query-dsl-must-not).

onelinerhub: [How can I use the "not equal" operator in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-the--not-equal--operator-in-elasticsearch)