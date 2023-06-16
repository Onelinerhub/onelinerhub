# How do I list all the indexes in Elasticsearch?
// plain

To list all the indexes in Elasticsearch, you can use the `_cat` API. The `_cat` API provides a convenient way to interact with the cluster and retrieve information about the nodes, indices, and shards.

## Example

```
$ curl -XGET 'localhost:9200/_cat/indices?v'
```

## Output example

```
health status index               uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   test_index          XXXXXXXXXXXXXXXXXX     5   1          0            0       5.3kb          5.3kb
```

The `_cat/indices` API provides the following information about each index:

- `health`: The health status of the index (green, yellow, or red).
- `status`: Whether the index is open or closed.
- `index`: The name of the index.
- `uuid`: A unique identifier for the index.
- `pri`: The number of primary shards in the index.
- `rep`: The number of replica shards in the index.
- `docs.count`: The number of documents in the index.
- `docs.deleted`: The number of deleted documents in the index.
- `store.size`: The size of the index in bytes.
- `pri.store.size`: The size of the primary shards in bytes.

For more information, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html).

onelinerhub: [How do I list all the indexes in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-list-all-the-indexes-in-elasticsearch)