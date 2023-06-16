# How can I use an elasticsearch aggregation filter?
// plain

An Elasticsearch aggregation filter is used to aggregate data from a search query. It allows you to group and filter the search results based on certain criteria.

For example, the following code block can be used to filter search results by the `category` field:

```
POST /_search
{
  "aggs": {
    "categories": {
      "terms": {
        "field": "category"
      }
    }
  }
}
```

The output of the above query would be a list of all the different categories present in the search results:

```
{
  ...
  "aggregations": {
    "categories": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "electronics",
          "doc_count": 4
        },
        {
          "key": "clothing",
          "doc_count": 2
        }
      ]
    }
  }
}
```

The code consists of the following parts:

- `POST /_search`: This tells Elasticsearch to perform a search query.
- `aggs`: This is the aggregation filter, which is used to group and filter the search results.
- `terms`: This is the aggregation type, which tells Elasticsearch to group the search results by the `category` field.

For more information on Elasticsearch aggregation filters, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html).

onelinerhub: [How can I use an elasticsearch aggregation filter?](https://onelinerhub.com/elasticsearch/how-can-i-use-an-elasticsearch-aggregation-filter)