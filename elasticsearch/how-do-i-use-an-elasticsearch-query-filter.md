# How do I use an elasticsearch query filter?
// plain

An Elasticsearch query filter is used to filter the search results of a query using a specific criteria. This can be done by adding a filter clause to the query.

For example, to filter a query for documents with a field `name` equal to `John`:

```
GET /_search
{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "name": "John"
        }
      }
    }
  }
}
```

This query will return documents that match the filter criteria, in this case documents with the field `name` equal to `John`.

The filter clause can also be used to filter on multiple criteria. For example, to filter documents with a field `name` equal to `John` and a field `age` greater than `30`:

```
GET /_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "name": "John"
          }
        },
        {
          "range": {
            "age": {
              "gt": 30
            }
          }
        }
      ]
    }
  }
}
```

This query will return documents that match both filter criteria, in this case documents with the field `name` equal to `John` and the field `age` greater than `30`.

The filter clause can also be used to filter on multiple criteria using logical operators. For example, to filter documents with a field `name` equal to `John` or a field `age` greater than `30`:

```
GET /_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "name": "John"
          }
        },
        {
          "range": {
            "age": {
              "gt": 30
            }
          }
        }
      ],
      "should": [
        {
          "term": {
            "name": "John"
          }
        },
        {
          "range": {
            "age": {
              "gt": 30
            }
          }
        }
      ]
    }
  }
}
```

This query will return documents that match either filter criteria, in this case documents with the field `name` equal to `John` or the field `age` greater than `30`.

## Helpful links
* [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
* [Elasticsearch Filters](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html)

onelinerhub: [How do I use an elasticsearch query filter?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-elasticsearch-query-filter)