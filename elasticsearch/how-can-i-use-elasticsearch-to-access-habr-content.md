# How can I use Elasticsearch to access Habr content?
// plain

Elasticsearch can be used to access Habr content in several ways.

1. Using the Elasticsearch API, you can create an index of Habr content and query it for specific results. For example, the following code will create an index called "habr" and query it for posts containing the word "Elasticsearch":

```
PUT /habr
{
  "mappings": {
    "post": {
      "properties": {
        "content": {
          "type": "text"
        }
      }
    }
  }
}

POST /habr/_search
{
  "query": {
    "match": {
      "content": "Elasticsearch"
    }
  }
}
```

## Output example

```
{
  "took": 11,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 2,
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": "habr",
        "_type": "post",
        "_id": "1",
        "_score": 0.2876821,
        "_source": {
          "content": "This is a post about Elasticsearch"
        }
      },
      {
        "_index": "habr",
        "_type": "post",
        "_id": "2",
        "_score": 0.2876821,
        "_source": {
          "content": "This is another post about Elasticsearch"
        }
      }
    ]
  }
}
```

2. You can also use the Elasticsearch Java API to access Habr content. The following code will create an index called "habr" and query it for posts containing the word "Elasticsearch":

```
// Create the index
CreateIndexRequest request = new CreateIndexRequest("habr");
CreateIndexResponse response = client.indices().create(request);

// Query the index
SearchRequest searchRequest = new SearchRequest("habr");
SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
searchSourceBuilder.query(QueryBuilders.matchQuery("content", "Elasticsearch"));
searchRequest.source(searchSourceBuilder);
SearchResponse searchResponse = client.search(searchRequest);

// Print the results
SearchHit[] searchHits = searchResponse.getHits().getHits();
for (SearchHit hit : searchHits) {
    System.out.println(hit.getSourceAsString());
}
```

## Output example

```
{"content": "This is a post about Elasticsearch"}
{"content": "This is another post about Elasticsearch"}
```

## Helpful links
- [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs.html)
- [Elasticsearch Java API](https://www.elastic.co/guide/en/elasticsearch/client/java-api/current/index.html)

onelinerhub: [How can I use Elasticsearch to access Habr content?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-access-habr-content)