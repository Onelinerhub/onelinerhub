# How can I troubleshoot an Elasticsearch cluster with a yellow status?
// plain

1. First, determine which nodes in the cluster are in a yellow status. This can be done by running the following command:
```
GET /_cluster/health
```
The output of the command will show the status of each node in the cluster.

2. If the yellow status is due to a single node, then investigate the node to determine the cause of the issue. This can be done by running the following command to get the node stats:
```
GET /_nodes/<node_id>/stats
```

3. If the yellow status is due to multiple nodes, then check the cluster settings to make sure they are correct. This can be done by running the following command:
```
GET /_cluster/settings
```

4. Check the cluster logs for errors or warnings that may be related to the yellow status. This can be done by running the following command:
```
GET /_cluster/logs
```

5. Check the cluster state to see if there are any shards that are in an unassigned state. This can be done by running the following command:
```
GET /_cluster/state
```

6. Check the network settings of the nodes in the cluster to make sure they are configured correctly.

7. Finally, if all else fails, restart the cluster and see if the yellow status persists. This can be done by running the following command:
```
POST /_cluster/restart
```

**Relevant Links**
- [Elasticsearch Cluster Health API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html)
- [Elasticsearch Node Stats API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-stats.html)
- [Elasticsearch Cluster Settings API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-update-settings.html)
- [Elasticsearch Cluster Logs API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-logs.html)
- [Elasticsearch Cluster State API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-state.html)
- [Elasticsearch Cluster Restart API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-restart.html)

onelinerhub: [How can I troubleshoot an Elasticsearch cluster with a yellow status?](https://onelinerhub.com/elasticsearch/how-can-i-troubleshoot-an-elasticsearch-cluster-with-a-yellow-status)