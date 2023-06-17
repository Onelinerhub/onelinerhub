# How do I use an elasticsearch query builder?
// plain

An Elasticsearch query builder is a tool that enables you to construct queries for Elasticsearch. It simplifies the process of creating and running Elasticsearch queries.

For example, the following code block uses the [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) to query for documents with the title "Elasticsearch Query Builder":

```
GET /_search
{
  "query": {
    "match": {
      "title": "Elasticsearch Query Builder"
    }
  }
}
```

This query will return all documents that contain the phrase "Elasticsearch Query Builder" in the title field.

The code block consists of the following parts:

- **GET /_search**: This is the request method and the endpoint for the query.
- **query**: This is the Elasticsearch query object.
- **match**: This is the query type, which in this case is a match query.
- **title**: This is the field that is being queried.
- **Elasticsearch Query Builder**: This is the query string.

Here are some useful links for learning more about Elasticsearch Query Builder:

- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- [Elasticsearch Query Builder Tutorial](https://www.elastic.co/blog/building-a-query-builder-for-elasticsearch)
- [Elasticsearch Query Builder Examples](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-examples.html)

onelinerhub: [How do I use an elasticsearch query builder?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-elasticsearch-query-builder)