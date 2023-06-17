# How can I use Elasticsearch to search for content?
// plain

Elasticsearch is a powerful search engine that can be used to search for content. It is built on top of Apache Lucene and provides a distributed, multitenant-capable full-text search engine. To use Elasticsearch to search for content, you need to first index the content. This can be done by sending a POST request to the Elasticsearch API with the content as the body of the request.

```
# Example code
curl -X POST "localhost:9200/my_index/_doc" -H 'Content-Type: application/json' -d'
{
  "title": "My Document",
  "body": "This is the content of my document."
}'
```

Once the content is indexed, you can then use the search API to query the indexed content. For example, you can use the following query to search for documents that contain the word "document":

```
# Example code
curl -X GET "localhost:9200/my_index/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "body": "document"
    }
  }
}'
```

The output of this query will be a JSON object that contains the documents that match the query.

```
# Output
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
    "total": 1,
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": "my_index",
        "_type": "_doc",
        "_id": "1",
        "_score": 0.2876821,
        "_source": {
          "title": "My Document",
          "body": "This is the content of my document."
        }
      }
    ]
  }
}
```

In summary, you can use Elasticsearch to search for content by indexing the content and then using the search API to query the indexed content.

## Code explanation
**

- `curl -X POST "localhost:9200/my_index/_doc" -H 'Content-Type: application/json' -d'`: This command sends a POST request to the Elasticsearch API with the content as the body of the request.

- `"query": { "match": { "body": "document" } }`: This is the query that is sent to the Elasticsearch API to search for documents that contain the word "document".

**## Helpful links**
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Elasticsearch API Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs.html)

onelinerhub: [How can I use Elasticsearch to search for content?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-search-for-content)