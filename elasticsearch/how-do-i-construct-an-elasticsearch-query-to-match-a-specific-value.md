# How do I construct an Elasticsearch query to match a specific value?
// plain

To construct an Elasticsearch query to match a specific value, you can use the `match` query. This query takes a field and a value as its parameters and returns documents that match the specified value in the specified field.

For example, to match documents with the value `foo` in the field `bar`, you could use the following query:

```
GET /_search
{
  "query": {
    "match": {
      "bar": "foo"
    }
  }
}
```

This query will return all documents that have the value `foo` in the field `bar`.

The parts of the query are as follows:

- `GET /_search`: This is the endpoint used to search for documents.
- `"query": {`: This indicates the start of the query.
- `"match": {`: This indicates that the `match` query is being used.
- `"bar": "foo"`: This specifies the field and value that should be matched.
- `}`: This indicates the end of the query.

For more information, see the [Elasticsearch documentation on the match query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html).

onelinerhub: [How do I construct an Elasticsearch query to match a specific value?](https://onelinerhub.com/elasticsearch/how-do-i-construct-an-elasticsearch-query-to-match-a-specific-value)