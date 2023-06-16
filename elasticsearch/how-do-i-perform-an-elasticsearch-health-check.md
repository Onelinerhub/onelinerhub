# How do I perform an elasticsearch health check?
// plain

An Elasticsearch health check is a process that helps ensure that the Elasticsearch cluster is running optimally. It involves checking the status of the cluster, verifying the nodes are running correctly, and checking the indices for any errors or issues.

To perform an Elasticsearch health check, you can use the `_cat/health` API endpoint. This will provide a quick overview of the cluster's health. The output will look something like this:

```
epoch      timestamp cluster        status node.total node.data shards pri relo init unassign pending_tasks max_task_wait_time active_shards_percent
1589192237 08:37:17 elasticsearch green           1         1      0   0    0    0        0             0                  -                100.0%
```

The output shows the following information:

- `epoch`: The time the health check was performed.
- `timestamp`: The date and time the health check was performed.
- `cluster`: The overall health of the cluster (green, yellow, or red).
- `node.total`: The total number of nodes in the cluster.
- `node.data`: The number of data nodes in the cluster.
- `shards`: The total number of shards in the cluster.
- `pri`: The number of primary shards in the cluster.
- `relo`: The number of relocating shards in the cluster.
- `init`: The number of initializing shards in the cluster.
- `unassign`: The number of unassigned shards in the cluster.
- `pending_tasks`: The number of pending tasks in the cluster.
- `max_task_wait_time`: The maximum wait time for tasks in the cluster.
- `active_shards_percent`: The percentage of active shards in the cluster.

For more detailed information, you can use the `_cluster/health` endpoint. This will provide a more detailed overview of the cluster's health.

For more information about performing an Elasticsearch health check, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-health.html).

onelinerhub: [How do I perform an elasticsearch health check?](https://onelinerhub.com/elasticsearch/how-do-i-perform-an-elasticsearch-health-check)