# How do I configure node roles in Elasticsearch?
// plain

To configure node roles in Elasticsearch, you can use the `node.roles` setting in the `elasticsearch.yml` configuration file. This setting is a list of roles that the node should have. The available roles are `master`, `data`, `ingest` and `ml`.

For example, to configure a node to be a master and data node, you can add the following to `elasticsearch.yml`:

```
node.roles: [master, data]
```

This will cause the node to act as both a master and data node.

The following is a list of the available roles and their meanings:
- `master`: A node with this role will be responsible for managing the cluster, including managing the state of the cluster and assigning shards to nodes.
- `data`: A node with this role will store and index data, and serve search requests.
- `ingest`: A node with this role will process data before it is indexed.
- `ml`: A node with this role will enable machine learning capabilities.

For more information, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html).

onelinerhub: [How do I configure node roles in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-configure-node-roles-in-elasticsearch)