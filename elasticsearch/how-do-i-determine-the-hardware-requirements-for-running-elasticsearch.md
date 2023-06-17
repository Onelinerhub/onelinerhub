# How do I determine the hardware requirements for running Elasticsearch?
// plain

The hardware requirements for running Elasticsearch depend on the size of the data set, the number of shards, and the number of replicas.

Generally, it is recommended to have a minimum of 4GB of RAM for each Elasticsearch node, and the number of cores should be equal to the number of shards.

For example, if your data set consists of 10GB of data with 5 shards and 1 replica, you would need at least 40GB of RAM and 5 cores.

To determine the exact hardware requirements for your cluster, you can use the [Elasticsearch Checkup](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-allocation.html#_check_cluster_allocation) tool. This tool will analyze your data set and provide a recommendation for the hardware requirements.

You can also use the Elasticsearch API to get the current cluster allocation settings. For example, the following code block will return the current cluster allocation settings:

```
GET /_cluster/allocation/explain
```

The output of the above code block will look something like this:

```
{
  "index": {
    "shard": 0,
    "primary": true,
    "current_state": "unassigned",
    "unassigned_info": {
      "reason": "ALLOCATION_FAILED",
      "at": "2020-08-03T09:15:13.631Z",
      "failed_allocation_attempts": 1,
      "details": "failed shard on node [_na_][Vl_QvjO-QlqgvDcV3K6yJg]: not enough disk space"
    }
  }
}
```

The output provides information about the shard, its current state, and the reason for any failed allocations. This information can help you determine the hardware requirements for running Elasticsearch.

## Helpful links

- [Elasticsearch Checkup](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-allocation.html#_check_cluster_allocation)
- [Elasticsearch API Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/allocation-explain.html)

onelinerhub: [How do I determine the hardware requirements for running Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-determine-the-hardware-requirements-for-running-elasticsearch)