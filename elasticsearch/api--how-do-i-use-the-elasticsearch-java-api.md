# api

How do I use the Elasticsearch Java API?
// plain

The Elasticsearch Java API allows you to interact with an Elasticsearch cluster using Java. It can be used to perform various operations such as creating, updating, and deleting indices, and adding, updating, and deleting documents.

Example code for creating an index using the Java API:
```
// Create an instance of the Java client
RestHighLevelClient client = new RestHighLevelClient(
    RestClient.builder(
        new HttpHost("localhost", 9200, "http")
    )
);

// Create an index
CreateIndexRequest request = new CreateIndexRequest("my_index");
CreateIndexResponse response = client.indices().create(request, RequestOptions.DEFAULT);
```

The code above creates an index named `my_index` using the Java API.

The code consists of the following parts:
1. Creating an instance of the Java client, `RestHighLevelClient`, which is used to interact with the Elasticsearch cluster.
2. Creating an `CreateIndexRequest` object with the index name.
3. Invoking the `create` method of the `client.indices()` object to create the index.

## Helpful links
- [Elasticsearch Java API](https://www.elastic.co/guide/en/elasticsearch/client/java-rest/current/java-rest-high.html)
- [CreateIndexRequest](https://www.elastic.co/guide/en/elasticsearch/client/java-rest/current/java-rest-high-create-index.html)

onelinerhub: [api

How do I use the Elasticsearch Java API?](https://onelinerhub.com/elasticsearch/api--how-do-i-use-the-elasticsearch-java-api)