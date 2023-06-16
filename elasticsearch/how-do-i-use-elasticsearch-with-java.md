# How do I use Elasticsearch with Java?
// plain

Elasticsearch is a popular open-source search engine built on Apache Lucene. It enables you to store, search, and analyze big volumes of data quickly and in near real-time.

Using Elasticsearch with Java requires three steps:

1. Install the Elasticsearch Java client: Add the following dependency to your project's pom.xml file:
```xml
<dependency>
    <groupId>org.elasticsearch.client</groupId>
    <artifactId>elasticsearch-rest-high-level-client</artifactId>
    <version>7.6.2</version>
</dependency>
```

2. Create an instance of the client:
```java
RestHighLevelClient client = new RestHighLevelClient(
    RestClient.builder(
        new HttpHost("localhost", 9200, "http")
    )
);
```

3. Use the client to perform operations:
```java
SearchRequest searchRequest = new SearchRequest("posts");
SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
searchSourceBuilder.query(QueryBuilders.matchQuery("title", "java"));
searchRequest.source(searchSourceBuilder);

SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
SearchHits hits = searchResponse.getHits();

System.out.println("Total hits: " + hits.getTotalHits());
for (SearchHit hit : hits.getHits()) {
    System.out.println(hit.getSourceAsString());
}
```
## Output example

```
Total hits: 2
{"title": "Java 8 Streams", "content": "Java 8 Streams..."}
{"title": "Java 11 Features", "content": "Java 11 Features..."}
```

The code above creates an instance of the client, then uses it to perform a search request on the `posts` index. The search query looks for documents with the title containing the word `java`. The output of the code prints out the total number of hits and the source of each document that matched the query.

## Helpful links
- [Elasticsearch Java Client](https://www.elastic.co/guide/en/elasticsearch/client/java-rest/7.6/java-rest-high.html)
- [Query Builders](https://www.elastic.co/guide/en/elasticsearch/client/java-rest/7.6/java-rest-high-query-builders.html)

onelinerhub: [How do I use Elasticsearch with Java?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-with-java)