# How can I use Elasticsearch to query data?
// plain

Elasticsearch is an open source, distributed search engine that is used to query data. It is based on the Apache Lucene library and provides an easy-to-use API for indexing and searching data.

The basic way to query data using Elasticsearch is by using its Query DSL. The Query DSL is a JSON-style domain-specific language that allows users to define queries in a structured way. For example, the following query will return all documents that match the term "example":

```
GET /_search
{
  "query": {
    "match": {
      "title": "example"
    }
  }
}
```

The result of the query will be a JSON object containing the matching documents.

In addition to the Query DSL, Elasticsearch also provides other query types such as the Multi-Match Query, Range Query, and more. For more information about the different query types and how to use them, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html).

Finally, it is also possible to use the Elasticsearch Java API to query data. This API provides an easy-to-use interface for interacting with the Elasticsearch cluster. For example, the following code will query the "example" index for documents that match the term "example":

```
SearchRequest searchRequest = new SearchRequest("example");
SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
searchSourceBuilder.query(QueryBuilders.matchQuery("title", "example"));
searchRequest.source(searchSourceBuilder);

SearchResponse searchResponse = client.search(searchRequest);
```

The result of the query will be a SearchResponse object which contains the matching documents.

For more information about using the Elasticsearch Java API, please refer to the [Elasticsearch Java API documentation](https://www.elastic.co/guide/en/elasticsearch/client/java-api/current/index.html).

onelinerhub: [How can I use Elasticsearch to query data?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-query-data)