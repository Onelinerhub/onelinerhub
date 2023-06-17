# How do I use Elasticsearch with ZGC?
// plain

Elasticsearch can be used with ZGC (Z Garbage Collector) to improve the performance of your Java applications. To use Elasticsearch with ZGC, you must first enable the ZGC JVM option. This is done by adding the following line to your jvm.options file:

```
-XX:+UseZGC
```

This will enable the Z Garbage Collector for your Elasticsearch cluster. Once enabled, you can then tune the ZGC parameters to optimize the performance of your Elasticsearch cluster. For example, to set the maximum heap size for ZGC, you can use the following line in your jvm.options file:

```
-XX:MaxHeapSize=<size>
```

Where `<size>` is the maximum heap size in bytes. You can also tune other ZGC parameters such as the pause target, the number of threads, and the number of regions.

In addition to tuning the ZGC parameters, you should also ensure that Elasticsearch is configured to take advantage of ZGC. This includes setting the `indices.memory.min_shard_index_buffer_size` and `indices.memory.max_shard_index_buffer_size` settings, as well as setting the `node.max_local_storage_nodes` setting.

## Helpful links
- [Z Garbage Collector](https://docs.oracle.com/en/java/javase/11/gctuning/z-garbage-collector.html)
- [Elasticsearch JVM Options](https://www.elastic.co/guide/en/elasticsearch/reference/current/jvm-options.html)
- [Elasticsearch Memory Settings](https://www.elastic.co/guide/en/elasticsearch/reference/current/memory-settings.html)

onelinerhub: [How do I use Elasticsearch with ZGC?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-with-zgc)