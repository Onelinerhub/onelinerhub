# How do I determine which version of Elasticsearch I am using?
// plain

To determine which version of Elasticsearch you are using, you can use the Elasticsearch API. To do this, you can use the following `GET` request:

```
GET _cat/nodes?v
```

The output of this request will look like this:

```
ip         heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
127.0.0.1           24          65   1    0.14    0.18     0.20 mdi       -      node1
127.0.0.2           24          65   1    0.14    0.18     0.20 mdi       *      node2
```

The `name` column in the output shows the version of Elasticsearch you are running. In this example, it is `node1` and `node2`.

You can also use the `version` API endpoint to check the version of Elasticsearch you are running. This endpoint will return the full version number, such as `7.8.1`. To do this, you can use the following `GET` request:

```
GET _cat/version
```

The output of this request will look like this:

```
7.8.1
```

The output is the full version number of Elasticsearch you are running.

## Helpful links
- [Elasticsearch API Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-nodes.html)
- [Elasticsearch Version API Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-version.html)

onelinerhub: [How do I determine which version of Elasticsearch I am using?](https://onelinerhub.com/elasticsearch/how-do-i-determine-which-version-of-elasticsearch-i-am-using)