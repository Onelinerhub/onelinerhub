# query

How do I create an Elasticsearch range query?
// plain

Creating an Elasticsearch range query is a simple process. The following example code will create a range query that will return documents with a timestamp field between two given dates:

```
GET /my_index/_search
{
  "query": {
    "range" : {
      "timestamp" : {
        "gte": "2020-01-01T00:00:00",
        "lte": "2020-01-31T00:00:00"
      }
    }
  }
}
```

The code above consists of the following parts:

* `GET /my_index/_search`: This is the API endpoint for searching in Elasticsearch.
* `{ "query": { ... } }`: This is the query body, which contains the range query.
* `"range" : { ... }`: This is the range query itself.
* `"timestamp" : { ... }`: This is the field that the range query should be run against.
* `"gte": "2020-01-01T00:00:00"`: This is the lower bound of the range query. It stands for "greater than or equal to".
* `"lte": "2020-01-31T00:00:00"`: This is the upper bound of the range query. It stands for "less than or equal to".

The output of the query should be a list of documents that match the given criteria.

For more information on Elasticsearch range queries, please refer to the following links:

* [Elasticsearch Range Queries](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-range-query.html)
* [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [query

How do I create an Elasticsearch range query?](https://onelinerhub.com/elasticsearch/query--how-do-i-create-an-elasticsearch-range-query)