# How do I configure the heap size for Elasticsearch?
// plain

The heap size for Elasticsearch can be configured by setting the ES_JAVA_OPTS environment variable. For example, the following code block sets the heap size to 4GB:

```
export ES_JAVA_OPTS="-Xms4g -Xmx4g"
```

The `-Xms` option sets the initial and minimum size of the heap, while the `-Xmx` option sets the maximum size of the heap. In the example above, the heap size is set to 4GB, with the minimum and maximum both set to 4GB.

It is recommended to set the minimum and maximum heap size to the same value. This will prevent Elasticsearch from having to resize the heap during runtime, which can cause performance issues.

For more information, please refer to the following links:

- [Elasticsearch Documentation: Configuring JVM Options](https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html)
- [Elasticsearch Documentation: Setting Environment Variables](https://www.elastic.co/guide/en/elasticsearch/reference/current/setting-environment-variables.html)

onelinerhub: [How do I configure the heap size for Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-configure-the-heap-size-for-elasticsearch)