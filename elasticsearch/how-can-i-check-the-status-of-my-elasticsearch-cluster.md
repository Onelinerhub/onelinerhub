# How can I check the status of my Elasticsearch cluster?
// plain

To check the status of an Elasticsearch cluster, you can use the [Cluster Health API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html):

```
curl -X GET "localhost:9200/_cluster/health?pretty"
```

This will return the status of the cluster, including the number of nodes, the cluster name, and the current status (green, yellow, or red).

For example, the following output indicates that the cluster is in a green status with 3 nodes:

```
{
  "cluster_name" : "elasticsearch",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 3,
  "active_primary_shards" : 10,
  "active_shards" : 20,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 100.0
}
```

The code block above consists of the following parts:

1. `curl -X GET "localhost:9200/_cluster/health?pretty"`: This is the command to send the request to the cluster health API.
2. `"cluster_name" : "elasticsearch"`: This is the name of the cluster.
3. `"status" : "green"`: This is the current status of the cluster (green, yellow, or red).
4. `"number_of_nodes" : 3`: This is the number of nodes in the cluster.
5. `"active_primary_shards" : 10`: This is the number of active primary shards in the cluster.
6. `"active_shards" : 20`: This is the number of active shards in the cluster.
7. `"active_shards_percent_as_number" : 100.0`: This is the percentage of active shards in the cluster.

onelinerhub: [How can I check the status of my Elasticsearch cluster?](https://onelinerhub.com/elasticsearch/how-can-i-check-the-status-of-my-elasticsearch-cluster)