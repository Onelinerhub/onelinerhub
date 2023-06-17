# How do I construct an Elasticsearch query using the bool query type?
// plain

The `bool` query type in Elasticsearch is a compound query that allows you to combine multiple queries together. The `bool` query type is used to combine `must`, `should`, `filter`, and `must_not` clauses.

For example, the following query will match documents that contain the term `Elasticsearch` in the `title` field and the term `query` in the `body` field.

```
GET /_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "Elasticsearch" }},
        { "match": { "body": "query" }}
      ]
    }
  }
}
```

The query is composed of the following parts:

- `GET /_search`: This is the request path.
- `query`: This is the root query object.
- `bool`: This is the query type.
- `must`: This is an array of clauses that must match for the query to match.
- `match`: This is the query type used to match documents.

## Helpful links

- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- [Compound Queries](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-compound-queries.html)

onelinerhub: [How do I construct an Elasticsearch query using the bool query type?](https://onelinerhub.com/elasticsearch/how-do-i-construct-an-elasticsearch-query-using-the-bool-query-type)