# How can I use Elasticsearch to match all elements in a given set?
// plain

Elasticsearch can be used to match all elements in a given set by using the `terms` query. This query is used to match documents that contain one or more exact terms specified in the `terms` array. For example, the following code block will match all elements in the `tags` array:

```
GET /_search
{
  "query": {
    "terms": {
      "tags": ["red", "green", "blue"]
    }
  }
}
```

The output of the above query will be documents that contain all of the elements in the `tags` array:

```
{
  "took": 4,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [
      {
        "_index": "my_index",
        "_type": "_doc",
        "_id": "1",
        "_score": 1.0,
        "_source": {
          "tags": ["red", "green", "blue"]
        }
      },
      {
        "_index": "my_index",
        "_type": "_doc",
        "_id": "2",
        "_score": 1.0,
        "_source": {
          "tags": ["red", "green", "blue", "yellow"]
        }
      }
    ]
  }
}
```

The code block consists of the following parts:

1. `GET /_search`: This is the request method and path for the search request.
2. `query`: This is the query object that contains the query parameters.
3. `terms`: This is the `terms` query object that contains the array of terms to match.
4. `tags`: This is the array of terms to match.

For more information on the `terms` query, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-terms-query.html).

onelinerhub: [How can I use Elasticsearch to match all elements in a given set?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-match-all-elements-in-a-given-set)