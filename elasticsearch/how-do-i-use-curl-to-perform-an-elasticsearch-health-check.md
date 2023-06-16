# How do I use cURL to perform an Elasticsearch health check?
// plain

To perform an Elasticsearch health check using cURL, you can use the following example code:

```
curl -XGET 'localhost:9200/_cluster/health?pretty'
```

The output of the command will show the health of the cluster, such as the status (green, yellow, or red), the number of nodes, and the number of data nodes:

```
{
  "cluster_name" : "elasticsearch",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 2,
  "active_primary_shards" : 5,
  "active_shards" : 10,
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

The code consists of the following parts:

- `curl` - the command line tool used to make the request
- `-XGET` - the type of request to make (in this case, a GET request)
- `localhost:9200` - the host and port of the Elasticsearch cluster
- `_cluster/health` - the endpoint to hit for the health check
- `?pretty` - an optional parameter to make the output more readable

For more information about using cURL to perform an Elasticsearch health check, see [this page](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html).

onelinerhub: [How do I use cURL to perform an Elasticsearch health check?](https://onelinerhub.com/elasticsearch/how-do-i-use-curl-to-perform-an-elasticsearch-health-check)