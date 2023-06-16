# How do I set the JVM heap size for Elasticsearch?
// plain

The JVM heap size for Elasticsearch can be set using the `ES_JAVA_OPTS` environment variable. This variable can be set in the `elasticsearch.yml` configuration file, which is located in the `config` directory of the Elasticsearch installation.

For example, to set the heap size to 8GB, add the following line to `elasticsearch.yml`:

```
ES_JAVA_OPTS: "-Xms8g -Xmx8g"
```

- `ES_JAVA_OPTS`: Environment variable to set the JVM heap size for Elasticsearch.
- `elasticsearch.yml`: Configuration file located in the `config` directory of the Elasticsearch installation.
- `-Xms8g`: Sets the initial heap size to 8GB.
- `-Xmx8g`: Sets the maximum heap size to 8GB.

## Helpful links
- [Elasticsearch JVM Options](https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html)
- [Configuring Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-configuration.html)

onelinerhub: [How do I set the JVM heap size for Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-set-the-jvm-heap-size-for-elasticsearch)