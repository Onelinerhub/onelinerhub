# How do I count the number of documents in an Elasticsearch index?
// plain

To count the number of documents in an Elasticsearch index, use the `count` API. This API returns the number of documents in the index without actually returning the documents themselves.

## Example code

```
GET /my_index/_count
```

## Output example

```
{
  "count": 100,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  }
}
```

The code consists of three parts:
- `GET`: The HTTP method used to send the request.
- `/my_index/_count`: The path to the index.
- `_count`: The API used to count the documents.

For more information, please refer to [the official Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-count.html).

onelinerhub: [How do I count the number of documents in an Elasticsearch index?](https://onelinerhub.com/elasticsearch/how-do-i-count-the-number-of-documents-in-an-elasticsearch-index)