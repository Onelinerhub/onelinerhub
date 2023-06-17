# How can I store and query zoned datetime values in Elasticsearch?
// plain

Elasticsearch provides the ability to store and query zoned datetime values using the [`date`](https://www.elastic.co/guide/en/elasticsearch/reference/current/date.html) datatype. It is important to note that the `date` datatype only supports ISO8601 formatted dates.

For example, to store a zoned datetime value of `2020-05-01T12:00:00+02:00`, you would use the following code:

```
PUT my_index/_doc/1
{
  "my_date": "2020-05-01T12:00:00+02:00"
}
```

To query for the zoned datetime value, you would use the `range` query:

```
GET my_index/_search
{
  "query": {
    "range": {
      "my_date": {
        "gte": "2020-05-01T12:00:00+02:00"
      }
    }
  }
}
```

The output of the query should look like this:

```
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [
      {
        "_index": "my_index",
        "_type": "_doc",
        "_id": "1",
        "_score": 1.0,
        "_source": {
          "my_date": "2020-05-01T12:00:00+02:00"
        }
      }
    ]
  }
}
```

In summary, storing and querying zoned datetime values in Elasticsearch can be done using the `date` datatype and the `range` query.

## Helpful links
- [Elasticsearch Date Datatype](https://www.elastic.co/guide/en/elasticsearch/reference/current/date.html)
- [Elasticsearch Range Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-range-query.html)

onelinerhub: [How can I store and query zoned datetime values in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-store-and-query-zoned-datetime-values-in-elasticsearch)