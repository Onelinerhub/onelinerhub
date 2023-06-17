# How can I check the status of a yellow index in Elasticsearch?
// plain

To check the status of a yellow index in Elasticsearch, you can use the `indices.status` API. This API will return the health, number of documents, size, and other information about the index.

## Example code

```
GET /my_index/_status
```

## Output example

```
{
   "my_index": {
      "status": "yellow",
      "number_of_shards": 5,
      "number_of_replicas": 1,
      "active_primary_shards": 5,
      "active_shards": 10,
      "relocating_shards": 0,
      "initializing_shards": 0,
      "unassigned_shards": 0,
      "delayed_unassigned_shards": 0,
      "number_of_pending_tasks": 0,
      "number_of_in_flight_fetch": 0,
      "task_max_waiting_in_queue_millis": 0,
      "active_shards_percent_as_number": 100.0
   }
}
```

The code above will return the status of the index, in this case it is "yellow". Additionally, the API will return the number of shards, replicas, active primary shards, active shards, relocating shards, initializing shards, unassigned shards, delayed unassigned shards, number of pending tasks, number of in flight fetch, task max waiting in queue millis, and active shards percent as number.

## Code explanation

- `GET`: HTTP verb used to retrieve information from the index
- `/my_index/_status`: the URL used to retrieve the status of the index

## Helpful links
- [Elasticsearch API Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-status.html)

onelinerhub: [How can I check the status of a yellow index in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-check-the-status-of-a-yellow-index-in-elasticsearch)