# How do I use an Elasticsearch term query?
// plain

A term query in Elasticsearch is used to search for a single term within a specific field. It is used to find exact matches of the specified term, and it is one of the most basic and commonly used queries.

Here is an example of a term query:

```
GET /_search
{
  "query": {
    "term": {
      "name": "John"
    }
  }
}
```

The output of the above query will be a list of documents that contain the exact term "John" in the field "name".

## Code explanation


- `GET /_search`: This is the HTTP request to the Elasticsearch server to execute a search query.
- `query`: This is the keyword used to specify the query to be executed.
- `term`: This is the keyword used to specify that a term query is to be executed.
- `name`: This is the field in which the specified term is to be searched.
- `John`: This is the term that is to be searched for.

Here are some ## Helpful links

- [Elasticsearch Term Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html)
- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [How do I use an Elasticsearch term query?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-elasticsearch-term-query)