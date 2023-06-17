# How can I use Elasticsearch to diagnose "yellow" issues?
// plain

Elasticsearch can be used to diagnose "yellow" issues by using the cluster health API. The cluster health API will return a status of either "green", "yellow" or "red" depending on the health of the cluster. If the status is "yellow", it indicates that the cluster is not operating optimally and further investigation is needed.

For example, the following code can be used to query the cluster health API:

```
GET /_cluster/health
```

The output of this query will be in the form of a JSON object, which will include the status of the cluster, the number of nodes, and the number of shards:

```
{
  "cluster_name" : "my-cluster",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 2,
  "active_primary_shards" : 12,
  "active_shards" : 20,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 8,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 71.42857142857143
}
```

If the status is "yellow", the next step is to investigate the cause of the issue. This can involve looking at the number of nodes, shards, and tasks, as well as any errors that may be present in the log files. It can also involve running further queries, such as the `_cat/nodes` API, to get more detailed information about the nodes in the cluster.

## Code explanation
**
  - `GET /_cluster/health`: Query the cluster health API
- **Links:**
  - [Elasticsearch Cluster Health API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html)
  - [Elasticsearch Cat API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat.html)

onelinerhub: [How can I use Elasticsearch to diagnose "yellow" issues?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-diagnose--yellow--issues)