# How can I rename an Elasticsearch index?
// plain

You can rename an Elasticsearch index using the `_reindex` API. This API allows you to copy documents from one index to another, and also allows you to change the destination index name. To rename an Elasticsearch index, you can use the following example code:

```
POST _reindex
{
  "source": {
    "index": "old_index_name"
  },
  "dest": {
    "index": "new_index_name"
  }
}
```

This code will copy all documents from the `old_index_name` index to the `new_index_name` index. The `old_index_name` index will remain in the cluster, and `new_index_name` will be the new name for the index.

The parts of the code are:

- `POST _reindex`: This is the API endpoint that will be used to copy documents from one index to another.
- `source`: This is the source index, which is the index that will be copied from.
- `index`: This is the name of the source index.
- `dest`: This is the destination index, which is the index that will be copied to.
- `index`: This is the name of the destination index.

## Helpful links

- [Elasticsearch Reindex API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html)
- [Elasticsearch Rename Index](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-rename-index.html)

onelinerhub: [How can I rename an Elasticsearch index?](https://onelinerhub.com/elasticsearch/how-can-i-rename-an-elasticsearch-index)