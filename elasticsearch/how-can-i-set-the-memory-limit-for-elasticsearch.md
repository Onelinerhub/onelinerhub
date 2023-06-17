# How can I set the memory limit for Elasticsearch?
// plain

To set the memory limit for Elasticsearch, you can use the `-Xms` and `-Xmx` parameters when starting the Elasticsearch service. These parameters specify the minimum and maximum amount of memory that the Java Virtual Machine (JVM) will allocate to the Elasticsearch process.

For example, to set the minimum memory to 2GB and the maximum memory to 4GB, you can use the following command:

```
bin/elasticsearch -Xms2g -Xmx4g
```

The parameters are:

- `-Xms`: Sets the initial size of the JVM heap.
- `-Xmx`: Sets the maximum size of the JVM heap.

You can find more information about these parameters in the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html).

onelinerhub: [How can I set the memory limit for Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-set-the-memory-limit-for-elasticsearch)