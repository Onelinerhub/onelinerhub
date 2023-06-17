# query

How do I write a nested query in Elasticsearch?
// plain

Nested queries allow you to query nested objects and returns objects that contain a nested object that matches the query. To write a nested query in Elasticsearch, you need to specify the nested query type and the path to the nested object.

For example, the following query will return documents that contain a nested object with the field “name” set to “John”:

```
GET /_search
{
    "query": {
        "nested": {
            "path": "nested_field",
            "query": {
                "term": {
                    "nested_field.name": "John"
                }
            }
        }
    }
}
```

The above query consists of the following parts:

- `GET /_search` - This is the request method and path used to search for documents.
- `query` - This is the query object that contains the query type and query parameters.
- `nested` - This is the query type used to query nested objects.
- `path` - This is the path to the nested object.
- `term` - This is the query type used to query for exact values.
- `nested_field.name` - This is the field within the nested object that is being queried.
- `John` - This is the value that is being queried.

For more information, please see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-nested-query.html).

onelinerhub: [query

How do I write a nested query in Elasticsearch?](https://onelinerhub.com/elasticsearch/query--how-do-i-write-a-nested-query-in-elasticsearch)