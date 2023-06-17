# How can I use the open source version of Elasticsearch?
// plain

You can use the open source version of Elasticsearch to build powerful search and analytics applications. Here is an example of how to use the Elasticsearch Java API to index and search documents:

```
// Create a client
Client client = new PreBuiltTransportClient(Settings.EMPTY)
    .addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("localhost"), 9300));

// Index a document
IndexResponse response = client.prepareIndex("twitter", "_doc", "1")
    .setSource(jsonBuilder()
        .startObject()
            .field("user", "kimchy")
            .field("postDate", new Date())
            .field("message", "trying out Elasticsearch")
        .endObject()
    )
    .get();

// Search for documents
SearchResponse searchResponse = client.prepareSearch("twitter")
    .setTypes("_doc")
    .setQuery(QueryBuilders.termQuery("user", "kimchy"))
    .get();
```

The code above will index a document with the user "kimchy" and message "trying out Elasticsearch" and then search for documents with the user "kimchy".

The code consists of the following parts:

1. Creating a client: This creates a client object which is used to communicate with the Elasticsearch cluster.
2. Indexing a document: This indexes a document using the Java API.
3. Searching for documents: This searches for documents using the Java API.

For more information about using the open source version of Elasticsearch, please refer to the official documentation:

- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Elasticsearch Java API](https://www.elastic.co/guide/en/elasticsearch/client/java-api/current/index.html)

onelinerhub: [How can I use the open source version of Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-the-open-source-version-of-elasticsearch)