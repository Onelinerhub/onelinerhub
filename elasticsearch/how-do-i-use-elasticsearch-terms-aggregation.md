# How do I use Elasticsearch terms aggregation?
// plain

The Elasticsearch Terms Aggregation is a type of aggregation that allows you to group values from a particular field together. It is useful for analyzing large datasets and finding patterns.

To use the Elasticsearch Terms Aggregation, you need to specify the field you want to group by and the type of aggregation. The following example code queries the `customers` index for the `age` field and uses the terms aggregation to group customers by age:

```
GET customers/_search
{
  "size": 0,
  "aggs": {
    "ages": {
      "terms": {
        "field": "age"
      }
    }
  }
}
```

The output of the above query would look like this:

```
{
  ...
  "aggregations": {
    "ages": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "18-24",
          "doc_count": 4
        },
        {
          "key": "25-34",
          "doc_count": 5
        },
        {
          "key": "35-44",
          "doc_count": 7
        },
        {
          "key": "45-54",
          "doc_count": 3
        },
        {
          "key": "55-64",
          "doc_count": 2
        }
      ]
    }
  }
  ...
}
```

## Code explanation


1. `GET customers/_search` - This specifies the index and type of documents to search.
2. `"size": 0` - This specifies that no documents should be returned, as only the aggregation results are needed.
3. `"aggs": { ... }` - This specifies the aggregation to use.
4. `"terms": { "field": "age" }` - This specifies the field to group by, in this case the `age` field.

## Helpful links

- [Elasticsearch Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html)
- [Terms Aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html)

onelinerhub: [How do I use Elasticsearch terms aggregation?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-terms-aggregation)