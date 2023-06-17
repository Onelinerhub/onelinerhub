# How do I configure Elasticsearch shards?
// plain

Sharding is a process of dividing an index into multiple pieces called shards. Each shard is an independent index in itself and can be stored on a separate node in the cluster. This allows for more efficient indexing and searching of large data sets.

To configure Elasticsearch shards, you need to specify the number of shards in the `elasticsearch.yml` configuration file. You can also set the number of replicas for each shard.

```
cluster.number_of_shards: 5
cluster.number_of_replicas: 1
```

The `cluster.number_of_shards` setting specifies the number of primary shards in the index. The `cluster.number_of_replicas` setting specifies the number of replicas for each primary shard.

Once the settings have been applied, the cluster will need to be restarted for the changes to take effect.

You can also use the API to configure shards. For example, the following API call can be used to set the number of shards and replicas for an index:

```
PUT /my_index
{
  "settings" : {
    "number_of_shards" : 5,
    "number_of_replicas" : 1
  }
}
```

The output of the API call would be:

```
{
  "acknowledged": true
}
```

For more information on configuring Elasticsearch shards, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-shards-allocation.html).

onelinerhub: [How do I configure Elasticsearch shards?](https://onelinerhub.com/elasticsearch/how-do-i-configure-elasticsearch-shards)