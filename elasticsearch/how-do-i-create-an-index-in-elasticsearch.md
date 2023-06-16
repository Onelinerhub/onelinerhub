# How do I create an index in Elasticsearch?
// plain

To create an index in Elasticsearch, you can use the `PUT` API endpoint. The syntax for creating an index is as follows:
```
PUT /<index_name>
```

For example, to create an index called `my_index`, the following command can be used:
```
PUT /my_index
```

The response to the above command will look like the following:
```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my_index"
}
```

You can also specify the number of shards and replicas while creating an index. The syntax for doing so is as follows:
```
PUT /<index_name>
{
  "settings" : {
    "number_of_shards" : <number_of_shards>,
    "number_of_replicas" : <number_of_replicas>
  }
}
```

For example, to create an index called `my_index` with 5 shards and 3 replicas, the following command can be used:
```
PUT /my_index
{
  "settings" : {
    "number_of_shards" : 5,
    "number_of_replicas" : 3
  }
}
```

The response to the above command will look like the following:
```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my_index"
}
```

**Parts of the code:**
1. `PUT`: The API endpoint used to create an index.
2. `<index_name>`: The name of the index to be created.
3. `number_of_shards`: The number of shards to be created with the index.
4. `number_of_replicas`: The number of replicas to be created with the index.

**## Helpful links**
1. [Elasticsearch Documentation - Create Index](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html)
2. [Elasticsearch Documentation - Index APIs](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-indexes.html)

onelinerhub: [How do I create an index in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-create-an-index-in-elasticsearch)