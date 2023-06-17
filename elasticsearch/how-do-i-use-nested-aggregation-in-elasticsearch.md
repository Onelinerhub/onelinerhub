# How do I use nested aggregation in Elasticsearch?
// plain

Nested aggregations in Elasticsearch allow you to aggregate data within nested objects. This can be used to answer questions such as “What are the top 5 most popular products in each category?”

## Example code

```
GET /_search
{
  "size": 0,
  "aggs": {
    "categories": {
      "nested": {
        "path": "products"
      },
      "aggs": {
        "top_products": {
          "terms": {
            "field": "products.name.keyword",
            "size": 5
          }
        }
      }
    }
  }
}
```

## Output example

```
{
  ...
  "aggregations" : {
    "categories" : {
      "doc_count" : 12,
      "top_products" : {
        "doc_count_error_upper_bound" : 0,
        "sum_other_doc_count" : 0,
        "buckets" : [
          {
            "key" : "Product A",
            "doc_count" : 4
          },
          {
            "key" : "Product B",
            "doc_count" : 3
          },
          {
            "key" : "Product C",
            "doc_count" : 2
          },
          {
            "key" : "Product D",
            "doc_count" : 1
          },
          {
            "key" : "Product E",
            "doc_count" : 1
          }
        ]
      }
    }
  }
  ...
}
```

## Code explanation


1. `GET /_search` - this is the endpoint used to send the aggregation query.
2. `"size": 0` - this specifies that no documents should be returned, only the aggregation results.
3. `"aggs": {` - this is the start of the aggregation section.
4. `"categories": {` - this is the name of the top-level aggregation.
5. `"nested": {` - this specifies that the aggregation should be done within a nested object.
6. `"path": "products"` - this specifies the path of the nested object.
7. `"terms": {` - this specifies that the aggregation should be done using terms.
8. `"field": "products.name.keyword"` - this specifies the field used for the terms aggregation.
9. `"size": 5` - this specifies the number of results to return.

## Helpful links

1. [Elasticsearch Documentation - Nested Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-nested-aggregation.html)
2. [Elasticsearch Documentation - Terms Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html)

onelinerhub: [How do I use nested aggregation in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-use-nested-aggregation-in-elasticsearch)