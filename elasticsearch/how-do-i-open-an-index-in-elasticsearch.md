# How do I open an index in Elasticsearch?
// plain

To open an index in Elasticsearch, you can use the `open` API. This API takes the index name as a parameter and returns a boolean value indicating the success of the operation.

```
PUT /my_index

{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 0
  }
}

PUT /my_index/_open

{
  "acknowledged": true
}
```

The example code above creates an index named `my_index` with 3 shards and 0 replicas, and then opens the index. The output of the second `PUT` call should be `{"acknowledged": true}`, indicating that the index was opened successfully.

The `open` API can also accept other parameters, such as `timeout` and `master_timeout`. For more information on these and other parameters, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-open-close.html).

onelinerhub: [How do I open an index in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-open-an-index-in-elasticsearch)