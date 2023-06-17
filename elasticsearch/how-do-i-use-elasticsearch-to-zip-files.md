# How do I use ElasticSearch to zip files?
// plain

ElasticSearch is not a tool used to zip files. However, you can use the [Compress API](https://www.elastic.co/guide/en/elasticsearch/reference/current/compress-endpoint.html) to compress files stored in the Elasticsearch cluster.

For example, you can use the `PUT` request to compress a file stored in the cluster:

```
PUT /my_index/my_type/my_id/_compress
```

The response of this request will look something like this:

```
{
  "_index": "my_index",
  "_type": "my_type",
  "_id": "my_id",
  "_version": 1,
  "result": "compressed",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 1
}
```

The `_shards` field indicates how many shards the document was indexed into. The `_seq_no` and `_primary_term` fields indicate the version of the document.

If you want to decompress the file, you can use the `GET` request:

```
GET /my_index/my_type/my_id/_decompress
```

This request will return the decompressed version of the file.

## Helpful links

- [Compress API](https://www.elastic.co/guide/en/elasticsearch/reference/current/compress-endpoint.html)

onelinerhub: [How do I use ElasticSearch to zip files?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-to-zip-files)