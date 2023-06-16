# How do I get all documents using Elasticsearch?
// plain

To get all documents using Elasticsearch, you need to use the [`search`](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html) API. The following example code will return all documents in a given index:

```
GET /my_index/_search
{
    "query": {
        "match_all": {}
    }
}
```
The output of this query will be a JSON object containing the documents:

```
{
    "took": 1,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 3,
            "relation": "eq"
        },
        "max_score": null,
        "hits": [
            {
                "_index": "my_index",
                "_type": "_doc",
                "_id": "1",
                "_score": null,
                "_source": {
                    "name": "John Doe"
                }
            },
            {
                "_index": "my_index",
                "_type": "_doc",
                "_id": "2",
                "_score": null,
                "_source": {
                    "name": "Jane Doe"
                }
            },
            {
                "_index": "my_index",
                "_type": "_doc",
                "_id": "3",
                "_score": null,
                "_source": {
                    "name": "Foo Bar"
                }
            }
        ]
    }
}
```

The code can be broken down into the following parts:

* `GET /my_index/_search` - This is the endpoint that is used to search the given index.
* `"query": { "match_all": {} }` - This is the query that is used to match all documents in the index.

For more information, please refer to the following links:

* [Elasticsearch Search API](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html)
* [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [How do I get all documents using Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-get-all-documents-using-elasticsearch)