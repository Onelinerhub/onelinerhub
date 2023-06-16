# How can I list the indexes in Elasticsearch?
// plain

To list the indexes in Elasticsearch, you can use the `_cat/indices` API. This API will return a list of all the indexes in the cluster.

For example, you can use the following cURL command to list all the indexes:
```
curl -XGET 'localhost:9200/_cat/indices?v&pretty'
```

The output of this command will look like this:
```
health status index    uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   myindex  s2G0-6jzTQ6Y3fh2tS9_KQ   5   1       1020            0     1.3mb         1.3mb
```

The output contains the following parts:
- **health**: The health status of the index.
- **status**: The open/close status of the index.
- **index**: The name of the index.
- **uuid**: The unique identifier of the index.
- **pri**: The number of primary shards of the index.
- **rep**: The number of replica shards of the index.
- **docs.count**: The number of documents in the index.
- **docs.deleted**: The number of deleted documents in the index.
- **store.size**: The total size of the index.
- **pri.store.size**: The total size of the primary shards of the index.

For more information, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html).

onelinerhub: [How can I list the indexes in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-list-the-indexes-in-elasticsearch)