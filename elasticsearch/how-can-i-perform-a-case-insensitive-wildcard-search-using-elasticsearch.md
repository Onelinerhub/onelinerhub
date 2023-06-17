# How can I perform a case-insensitive wildcard search using Elasticsearch?
// plain

A wildcard search in Elasticsearch using a case-insensitive query is possible by using the `lowercase_expanded_terms` parameter.

## Example code

```
GET /my_index/_search
{
  "query": {
    "wildcard": {
      "my_field": {
        "value": "*test*",
        "lowercase_expanded_terms": false
      }
    }
  }
}
```

This query will return all documents that contain the term `test` in the `my_field` field, regardless of the case.

The `lowercase_expanded_terms` parameter is set to `false` by default, so it is not necessary to set it explicitly.

## Code explanation


- `GET /my_index/_search` - the endpoint used to send the query to Elasticsearch
- `"query": { "wildcard": { "my_field": { "value": "*test*"` - the `wildcard` query used to perform the search, with `my_field` as the field to search in and `*test*` as the value to search for
- `"lowercase_expanded_terms": false` - the parameter used to make the search case-insensitive

## Helpful links

- [Elasticsearch Wildcard Query Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-wildcard-query.html)
- [Elasticsearch Case-Insensitive Wildcard Queries](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-wildcard-query.html#_case_insensitive_wildcard_queries)

onelinerhub: [How can I perform a case-insensitive wildcard search using Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-perform-a-case-insensitive-wildcard-search-using-elasticsearch)