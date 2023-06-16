# How do I check the status of my Elasticsearch cluster?
// plain

To check the status of an Elasticsearch cluster, you can use the Cluster Health API.

Example request:
```
curl -XGET 'localhost:9200/_cluster/health?pretty'
```

Example output:
```
{
  "cluster_name" : "elasticsearch_jdoe",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 3,
  "active_primary_shards" : 8,
  "active_shards" : 16,
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

The output of the request above will provide the following information:

* `cluster_name`: The name of the cluster.
* `status`: The current status of the cluster. Possible values are `green`, `yellow`, or `red`.
* `timed_out`: Whether the request timed out or not.
* `number_of_nodes`: The number of nodes in the cluster.
* `number_of_data_nodes`: The number of data nodes in the cluster.
* `active_primary_shards`: The number of active primary shards in the cluster.
* `active_shards`: The number of active shards in the cluster.
* `relocating_shards`: The number of relocating shards in the cluster.
* `initializing_shards`: The number of initializing shards in the cluster.
* `unassigned_shards`: The number of unassigned shards in the cluster.
* `delayed_unassigned_shards`: The number of delayed unassigned shards in the cluster.
* `number_of_pending_tasks`: The number of pending tasks in the cluster.
* `number_of_in_flight_fetch`: The number of in-flight fetch operations in the cluster.
* `task_max_waiting_in_queue_millis`: The maximum waiting time for tasks in the queue in milliseconds.
* `active_shards_percent_as_number`: The percentage of active shards in the cluster.

For more information on the Cluster Health API, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html).

onelinerhub: [How do I check the status of my Elasticsearch cluster?](https://onelinerhub.com/elasticsearch/how-do-i-check-the-status-of-my-elasticsearch-cluster)