# How can I monitor performance metrics with Elasticsearch?
// plain

Elasticsearch provides a wide range of performance metrics which can be monitored using the [Elasticsearch Monitoring APIs](https://www.elastic.co/guide/en/elasticsearch/reference/current/monitoring.html).

Using the Monitoring APIs, you can get detailed information about the performance of your cluster, nodes, and indices. For example, the following code snippet shows how to retrieve the cluster health metrics using the Cluster Health API:

```
GET /_cluster/health
```

The output of this API call will be a JSON object containing the following performance metrics:

- Cluster Name
- Status
- Number of Nodes
- Number of Data Nodes
- Active Primary Shards
- Active Shards
- Relocating Shards
- Initializing Shards
- Unassigned Shards

You can also use the Node Stats API to retrieve detailed information about the performance of each node in the cluster:

```
GET /_nodes/stats
```

The output of this API call will be a JSON object containing the following performance metrics:

- Operating System
- JVM
- Process
- Thread Pool
- File System
- Transports
- HTTP
- Breakers
- Scripts
- Discovery
- Ingest
- Cgroup

You can also use the Index Stats API to retrieve detailed information about the performance of each index in the cluster:

```
GET /_stats
```

The output of this API call will be a JSON object containing the following performance metrics:

- Number of Documents
- Number of Deleted Documents
- Primary Store Size
- Total Store Size
- Indexing Throughput
- Search Throughput
- Refresh Throughput
- Segments Count
- Memory Usage
- Query Cache Size
- Field Data Cache Size
- Filter Cache Size
- Flush Throughput

Using the Monitoring APIs, you can monitor the performance of your Elasticsearch cluster, nodes, and indices.

onelinerhub: [How can I monitor performance metrics with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-monitor-performance-metrics-with-elasticsearch)