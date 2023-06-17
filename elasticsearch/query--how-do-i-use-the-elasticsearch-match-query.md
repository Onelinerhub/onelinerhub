# query

How do I use the Elasticsearch match query?
// plain

The Elasticsearch match query is a query used to search for documents that match a specified text, number, date, or boolean value. It is the most commonly used query in Elasticsearch and is used to search for one or more terms in a single field. It is a full-text search query that supports fuzzy matching and phrase queries.

The following example code demonstrates how to use the match query:

```
GET /_search
{
  "query": {
    "match": {
      "title": "Elasticsearch Query"
    }
  }
}
```

This example search looks for documents that contain the phrase "Elasticsearch Query" in the title field.

The parts of the query are as follows:

* `GET /_search` - This indicates that the query will be run against the Elasticsearch search API.
* `query` - This is the main query object, which contains one or more query clauses.
* `match` - This is the type of query clause being used. In this case, it is a match query.
* `title` - This is the field that is being searched.
* `Elasticsearch Query` - This is the text that is being searched for.

For more information on the match query, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html).

onelinerhub: [query

How do I use the Elasticsearch match query?](https://onelinerhub.com/elasticsearch/query--how-do-i-use-the-elasticsearch-match-query)