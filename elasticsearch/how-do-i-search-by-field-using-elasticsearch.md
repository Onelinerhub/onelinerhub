# How do I search by field using Elasticsearch?
// plain

To search by field using Elasticsearch, you need to use the `term` query. The `term` query is used to search for a specific value in a specific field. For example, the following query searches for documents with the value `example` in the field `title`:

```
GET /_search
{
  "query": {
    "term": {
      "title": "example"
    }
  }
}
```

The output of this query will be a list of documents that contain the word `example` in the `title` field.

The `term` query has the following parts:

- `query`: This is the root element of the query.
- `term`: This is the type of query being used.
- `title`: This is the field being searched.
- `example`: This is the value being searched for.

For more information about the `term` query, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html).

onelinerhub: [How do I search by field using Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-search-by-field-using-elasticsearch)