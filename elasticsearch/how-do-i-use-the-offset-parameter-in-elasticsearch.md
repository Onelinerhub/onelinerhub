# How do I use the offset parameter in Elasticsearch?
// plain

The offset parameter in Elasticsearch is used to control the starting point from which the search results are returned. It is useful when you want to page through a large result set.

For example, the following code will return the first 10 results starting from the 11th result:
```
GET /_search
{
  "from": 10,
  "size": 10
}
```

The `from` parameter is the offset parameter, and it is set to 10 in this example. This means that the results returned will start from the 11th result.

The `size` parameter is the number of results to return. In this example, it is set to 10, so the results returned will be the 11th to 20th result.

Here are some useful links for further reading:
- [Elasticsearch Offset Parameter](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-from-size.html)
- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [How do I use the offset parameter in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-use-the-offset-parameter-in-elasticsearch)