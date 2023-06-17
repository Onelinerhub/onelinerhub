# How can I use the Elasticsearch REST API?
// plain

The Elasticsearch REST API allows you to interact with the Elasticsearch cluster via the HTTP protocol. It allows you to search, index, update, and delete data in the cluster.

For example, you can use the `GET` method to retrieve a document from the cluster:

```
curl -XGET "localhost:9200/my_index/my_type/1"
```

## Output example

```json
{
    "_index": "my_index",
    "_type": "my_type",
    "_id": "1",
    "_version": 1,
    "found": true,
    "_source": {
        "name": "John Doe",
        "age": 35
    }
}
```

You can also use the `POST` method to create a new document in the cluster:

```
curl -XPOST "localhost:9200/my_index/my_type" -H 'Content-Type: application/json' -d'
{
    "name": "Jane Doe",
    "age": 25
}
'
```

## Output example

```
{"_index":"my_index","_type":"my_type","_id":"2","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0}}
```

The Elasticsearch REST API also supports other methods such as `PUT`, `DELETE`, and `HEAD`. You can find more information about the API in the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/rest-apis.html).

onelinerhub: [How can I use the Elasticsearch REST API?](https://onelinerhub.com/elasticsearch/how-can-i-use-the-elasticsearch-rest-api)