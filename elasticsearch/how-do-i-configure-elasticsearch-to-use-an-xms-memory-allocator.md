# How do I configure elasticsearch to use an XMS memory allocator?
// plain

Configuring elasticsearch to use an XMS memory allocator requires the following steps:

1. Set the environment variable `ES_JAVA_OPTS` to the following value: `-XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1`

2. Create the file `jvm.options` in the config directory of elasticsearch and add the following line to it: `-XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1`

3. Restart elasticsearch

The above steps will configure elasticsearch to use the XMS memory allocator.

```
$ export ES_JAVA_OPTS="-XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1"
```

## Helpful links
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/jvm-options.html)
- [XMS Memory Allocator Documentation](https://docs.oracle.com/en/java/javase/13/vmoptions/xms-memory-allocator.html)

onelinerhub: [How do I configure elasticsearch to use an XMS memory allocator?](https://onelinerhub.com/elasticsearch/how-do-i-configure-elasticsearch-to-use-an-xms-memory-allocator)