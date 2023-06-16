# How do I use the Elasticsearch API?
// plain

The Elasticsearch API allows users to interact with the Elasticsearch search engine using a RESTful API. The API can be used for indexing documents, creating and managing indices, and performing search and aggregation queries.

Example code to index a document:
```
POST /my_index/my_type/1
{
  "title": "Elasticsearch API",
  "text": "This is a guide to using the Elasticsearch API"
}
```

This will create a document with an ID of 1 in the index `my_index` and type `my_type`.

To perform a search query, you can use the `_search` endpoint:
```
GET /my_index/_search
{
  "query": {
    "match": {
      "text": "Elasticsearch API"
    }
  }
}
```

This will return any documents which contain the phrase "Elasticsearch API".

## Helpful links
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Elasticsearch API Cheat Sheet](https://www.elastic.co/guide/en/elasticsearch/reference/current/api-reference.html)

onelinerhub: [How do I use the Elasticsearch API?](https://onelinerhub.com/elasticsearch/how-do-i-use-the-elasticsearch-api)