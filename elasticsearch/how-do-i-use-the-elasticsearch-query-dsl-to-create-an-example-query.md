# How do I use the Elasticsearch Query DSL to create an example query?
// plain

The Elasticsearch Query DSL (Domain Specific Language) is a powerful query language that allows you to define queries in JSON format. It is used to search and filter documents stored in Elasticsearch.

To create an example query, you can use the following code block:

```
GET /_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "title": "Elasticsearch"
          }
        },
        {
          "term": {
            "category": "search"
          }
        }
      ]
    }
  }
}
```

This code block will search for documents with the title "Elasticsearch" and the category "search".

The code block consists of the following parts:

- `GET /_search`: This is the request sent to the Elasticsearch cluster.
- `query`: This is the query object used to define the query.
- `bool`: This is a boolean query used to combine multiple queries.
- `must`: This is an array of queries that must match for the document to be returned.
- `match`: This is a query used to match documents that contain the specified text.
- `term`: This is a query used to match documents with the specified term.

No output is returned from this example query.

For more information, see the [Elasticsearch Query DSL documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html).

onelinerhub: [How do I use the Elasticsearch Query DSL to create an example query?](https://onelinerhub.com/elasticsearch/how-do-i-use-the-elasticsearch-query-dsl-to-create-an-example-query)