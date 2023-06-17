# How do I create an elasticsearch query that is similar to an existing query?
// plain

Creating an elasticsearch query that is similar to an existing query is relatively simple. The basic steps are as follows:
1. Identify the existing query.
2. Analyze the existing query, including the fields, values, and operators used.
3. Construct a new query using the same fields, values, and operators.

For example, if the existing query is:
```
GET /_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "title": "elasticsearch"
          }
        },
        {
          "range": {
            "price": {
              "gte": 10,
              "lte": 20
            }
          }
        }
      ]
    }
  }
}
```

The new query could be:
```
GET /_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "title": "kibana"
          }
        },
        {
          "range": {
            "price": {
              "gte": 10,
              "lte": 20
            }
          }
        }
      ]
    }
  }
}
```

The two queries are similar in structure, with the only difference being the value of the `title` field.

## Code explanation
**
1. `GET /_search` - indicates the type of query being made.
2. `"query": { "bool": { "must": [ ... ] } }` - indicates the type of query being made (a boolean query with a `must` clause).
3. `"match": { "title": "elasticsearch" }` - indicates a match query for the `title` field with a value of `elasticsearch`.
4. `"range": { "price": { "gte": 10, "lte": 20 } }` - indicates a range query for the `price` field with a minimum value of `10` and a maximum value of `20`.

**## Helpful links**
- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- [Elasticsearch Boolean Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html)
- [Elasticsearch Match Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html)
- [Elasticsearch Range Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-range-query.html)

onelinerhub: [How do I create an elasticsearch query that is similar to an existing query?](https://onelinerhub.com/elasticsearch/how-do-i-create-an-elasticsearch-query-that-is-similar-to-an-existing-query)