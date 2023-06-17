# How can I view the version history of Elasticsearch?
// plain

Using the Elasticsearch API, you can view the version history of Elasticsearch. The following example code will return the version history of Elasticsearch:

```
GET /_cat/nodes?v
```

This will return a list of nodes and their versions, e.g.:

```
ip         heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
127.0.0.1           66          39   6    0.10    0.14     0.17 mdi       -      node1
127.0.0.2           54          37   6    0.09    0.12     0.15 mdi       *      node2
127.0.0.3           66          38   6    0.08    0.11     0.15 mdi       -      node3
```

The `node.role` column indicates if the node is a master or data node. The `master` column indicates which node is the master node. The `name` column shows the node name. The `v` parameter in the command indicates that the version should be included in the output.

You can also use the following command to view the version of a specific node:

```
GET /_nodes/node_name
```

This will return the version of the specific node, e.g.:

```
{
  "name" : "node_name",
  "version" : "7.9.2"
}
```

## Helpful links

- [Elasticsearch API - View Version History](https://www.elastic.co/guide/en/elasticsearch/reference/7.9/cat-nodes.html)
- [Elasticsearch API - View Version of Specific Node](https://www.elastic.co/guide/en/elasticsearch/reference/7.9/cat-nodes.html)

onelinerhub: [How can I view the version history of Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-view-the-version-history-of-elasticsearch)