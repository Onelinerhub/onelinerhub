# aggregation

How do I use Elasticsearch terms aggregation?
// plain

The **Elasticsearch terms aggregation** is a powerful tool for data analysis and exploration. It allows you to quickly and easily group and summarize large datasets. It is an important part of the Elasticsearch Query DSL (Domain Specific Language).

The following example shows how to use the terms aggregation to group documents by a particular field. It uses the `terms` aggregation to group documents by the `category` field and then calculates the average `price` for each group.

```
GET /_search
{
  "size": 0,
  "aggs": {
    "category_groups": {
      "terms": {
        "field": "category"
      },
      "aggs": {
        "avg_price": {
          "avg": {
            "field": "price"
          }
        }
      }
    }
  }
}
```

The output of the example query would look something like this:

```
{
  "took": 5,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 10,
    "max_score": 0,
    "hits": []
  },
  "aggregations": {
    "category_groups": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "electronics",
          "doc_count": 5,
          "avg_price": {
            "value": 20.0
          }
        },
        {
          "key": "clothing",
          "doc_count": 5,
          "avg_price": {
            "value": 10.0
          }
        }
      ]
    }
  }
}
```

The `terms` aggregation can be used to group documents by any field, and can be combined with other aggregations to produce complex summaries.

**Parts of the code:**
- `GET /_search`: This is the query that is sent to Elasticsearch to retrieve the documents.
- `size: 0`: This tells Elasticsearch to not return any documents, only the aggregations.
- `aggs`: This is the part of the query that defines the aggregations to be performed.
- `terms`: This is the aggregation that groups documents by a field.
- `field`: This is the field that the documents will be grouped by.
- `aggs`: This is the part of the query that defines the sub-aggregations to be performed.
- `avg`: This is the aggregation that calculates the average of a field.
- `field`: This is the field that the average will be calculated for.

**## Helpful links**
- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- [Elasticsearch Terms Aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html)

onelinerhub: [aggregation

How do I use Elasticsearch terms aggregation?](https://onelinerhub.com/elasticsearch/aggregation--how-do-i-use-elasticsearch-terms-aggregation)