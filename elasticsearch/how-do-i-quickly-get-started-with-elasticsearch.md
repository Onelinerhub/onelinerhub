# How do I quickly get started with Elasticsearch?
// plain

1. Download and install the latest version of [Elasticsearch](https://www.elastic.co/downloads/elasticsearch) on your local machine.

2. Start up the Elasticsearch server by running the following command: ```bin/elasticsearch```

3. To verify that the server is running correctly, send an HTTP request using curl: ```curl -X GET "localhost:9200"```

4. The response should look similar to the following:
```
{
  "name" : "node-1",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "abc123",
  "version" : {
    "number" : "7.6.2",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "abc123",
    "build_date" : "2020-03-26T06:34:37.794943Z",
    "build_snapshot" : false,
    "lucene_version" : "8.4.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

5. You can now start indexing data in Elasticsearch. For example, here is a command to index a document:
```curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "name": "John Doe"
}
'
```

6. You can also query the indexed data. Here is an example query:
```curl -X GET "localhost:9200/customer/_doc/1?pretty"
```

7. For more information on how to use Elasticsearch, see [the official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).

onelinerhub: [How do I quickly get started with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-quickly-get-started-with-elasticsearch)