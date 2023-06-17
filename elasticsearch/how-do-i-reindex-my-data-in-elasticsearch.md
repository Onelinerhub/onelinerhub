# How do I reindex my data in Elasticsearch?
// plain

Reindexing in Elasticsearch is the process of changing the existing index structure or settings. This can be done in two ways:

1. Using the Reindex API:

The Reindex API allows you to copy documents from one index to another, possibly changing the index settings and/or the mapping along the way.

## Example

```
POST _reindex
{
  "source": {
    "index": "my_source_index"
  },
  "dest": {
    "index": "my_dest_index"
  }
}
```

## Output example

```
{
  "took": 9,
  "timed_out": false,
  "_scroll_id": "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAD4WYm9laVYtZndUQlNsdDcwakFMNjU1QQ==",
  "total": 5,
  "updated": 0,
  "created": 5,
  "deleted": 0,
  "batches": 1,
  "version_conflicts": 0,
  "noops": 0,
  "retries": {
    "bulk": 0,
    "search": 0
  },
  "throttled_millis": 0,
  "requests_per_second": -1.0,
  "throttled_until_millis": 0
}
```

The parts of the code are:
- The `POST` command, to send the request to the server.
- The `_reindex` endpoint, which is the Elasticsearch API used for reindexing.
- The `source` and `dest` objects, which define the source and destination indices.
- Parameters such as `_scroll_id`, `total`, `created`, and `deleted`, which provide information about the reindexing process.

2. Using Logstash:

Logstash is a data processing pipeline that allows you to transform data from one format to another. You can use Logstash to reindex Elasticsearch data by setting up a pipeline that reads from the source index, transforms the data if needed, and then writes to the destination index.

## Helpful links
- [Reindex API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html)
- [Logstash Documentation](https://www.elastic.co/guide/en/logstash/current/index.html)

onelinerhub: [How do I reindex my data in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-reindex-my-data-in-elasticsearch)