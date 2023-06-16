# How do I delete an index in Elasticsearch?
// plain

To delete an index in Elasticsearch, use the `DELETE` method on the `/_cat/indices` endpoint. For example:

```
DELETE /my_index
```

This will delete the index `my_index`.

The following parts make up the example code:

* `DELETE`: This is the HTTP method used for deleting an index.
* `/my_index`: This is the name of the index to be deleted.

If the index was successfully deleted, the response should be a `200` status code.

## Helpful links

* [Elasticsearch Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-delete-index.html)
* [Elasticsearch API Conventions](https://www.elastic.co/guide/en/elasticsearch/reference/current/api-conventions.html)

onelinerhub: [How do I delete an index in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-delete-an-index-in-elasticsearch)