# How do I write an Elasticsearch query example?
// plain

An Elasticsearch query is a request to search the contents of one or more indices. To write an Elasticsearch query example, you will need to specify the index(es) you want to search, the type of query you want to make (e.g. match, term, range, etc.), and any parameters associated with the query.

For example, the following query will search for documents containing the term "Elasticsearch" in the "title" field of an index named "blog":

```
GET /blog/_search
{
  "query": {
    "match": {
      "title": "Elasticsearch"
    }
  }
}
```

This query consists of the following parts:

* **GET /blog/_search**: This specifies the index (blog) and the search endpoint (/_search).
* **query**: This is the root object of the query and contains the query type (match).
* **title**: This is the field in which the query should look for the term "Elasticsearch".

For more information on writing Elasticsearch queries, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html).

onelinerhub: [How do I write an Elasticsearch query example?](https://onelinerhub.com/elasticsearch/how-do-i-write-an-elasticsearch-query-example)