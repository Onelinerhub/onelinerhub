# How can I create an Elasticsearch query using the Query DSL?
// plain

The Query DSL in Elasticsearch is a powerful query language for searching data. It is based on the JSON format and allows you to create complex queries that can be used to search and filter documents in an Elasticsearch index.

To create an Elasticsearch query using the Query DSL, you will need to define the query in a JSON format. Here is an example of a simple query that will match documents with the field "title" containing the term "Elasticsearch":

```
{
  "query": {
    "match" : {
      "title" : "Elasticsearch"
    }
  }
}
```

The query consists of two parts:

1. The `query` object - This is the root object of the query and contains the query parameters.

2. The `match` clause - This is the specific query clause that will perform the search. In this example, it will match documents with the field "title" containing the term "Elasticsearch".

This query can then be used in the Elasticsearch API to search an index.

For more information on the Query DSL, please see the [Elasticsearch Query DSL documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html).

onelinerhub: [How can I create an Elasticsearch query using the Query DSL?](https://onelinerhub.com/elasticsearch/how-can-i-create-an-elasticsearch-query-using-the-query-dsl)