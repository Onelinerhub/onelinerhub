# How do I explain Elasticsearch to a beginner?
// plain

Elasticsearch is a powerful open-source search engine built on top of Apache Lucene. It is a distributed, RESTful search and analytics engine capable of solving a growing number of use cases.

Elasticsearch provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. It stores and indexes data using a document-oriented data model, making it easier to search and analyze data quickly.

## Example code

```
GET /my_index/_search
{
  "query": {
    "match_all": {}
  }
}
```

## Output example

```
{
  "took": 3,
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
    "max_score": null,
    "hits": [
      {
        "_index": "my_index",
        "_type": "_doc",
        "_id": "1",
        "_score": null,
        "_source": {
          "title": "My first document",
          "text": "This is my first document"
        }
      },
      {
        "_index": "my_index",
        "_type": "_doc",
        "_id": "2",
        "_score": null,
        "_source": {
          "title": "My second document",
          "text": "This is my second document"
        }
      }
    ]
  }
}
```

## Code explanation

- `GET`: This is the HTTP method used for the request.
- `/my_index/_search`: This is the Elasticsearch endpoint for running searches.
- `query`: This is the query object which contains the query to be executed.
- `match_all`: This is the query type used to match all documents in the index.

## Helpful links
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Elasticsearch Tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)

onelinerhub: [How do I explain Elasticsearch to a beginner?](https://onelinerhub.com/elasticsearch/how-do-i-explain-elasticsearch-to-a-beginner)