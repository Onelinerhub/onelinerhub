# How can I use Elasticsearch to find a document by a specific field?
// plain

Elasticsearch can be used to find a document by a specific field using the `match` query. This query looks for documents that contain a specified field with a specified value. For example, to search for a document that contains the field `title` with the value `example`:

```
GET /_search
{
  "query": {
    "match": {
      "title": "example"
    }
  }
}
```

The output of this query would be the documents that contain the field `title` with the value `example`:

```
{
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
          "title": "example"
        }
      }
    ]
  }
}
```

The parts of the code are as follows:

1. `GET /_search` - This is the endpoint for the search query.
2. `"query": {` - This is the start of the query body.
3. `"match": {` - This is the start of the `match` query.
4. `"title": "example"` - This is the field and value to match.
5. `}` - This closes the `match` query.
6. `}` - This closes the query body.

## Helpful links

- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- [Match Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html)

onelinerhub: [How can I use Elasticsearch to find a document by a specific field?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-find-a-document-by-a-specific-field)