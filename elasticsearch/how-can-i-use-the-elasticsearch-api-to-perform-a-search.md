# How can I use the Elasticsearch API to perform a search?
// plain

You can use the Elasticsearch API to perform a search by using the `_search` endpoint. For example, to perform a basic search using the `GET` method, you can use the following code:

```
GET /_search
{
  "query": {
    "match_all": {}
  }
}
```

This will return all documents in the index. You can also use more complex search queries to return more specific results. For example, to search for documents that contain the word `elasticsearch`, you can use the following code:

```
GET /_search
{
  "query": {
    "match": {
      "message": "elasticsearch"
    }
  }
}
```

This will return all documents that contain the word `elasticsearch`.

## Code explanation

- `GET` method: to send the search query to the `_search` endpoint
- `query`: to define the search query
- `match_all`: to return all documents in the index
- `match`: to search for documents that contain a specific word

## Helpful links
- [Elasticsearch API Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html)
- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [How can I use the Elasticsearch API to perform a search?](https://onelinerhub.com/elasticsearch/how-can-i-use-the-elasticsearch-api-to-perform-a-search)