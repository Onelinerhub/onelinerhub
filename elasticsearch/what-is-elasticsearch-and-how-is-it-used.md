# What is Elasticsearch and how is it used?
// plain

Elasticsearch is an open source search engine built on Apache Lucene. It provides a distributed, multitenant-capable full-text search engine with a RESTful web interface and schema-free JSON documents. Elasticsearch is used for fast searches and analysis of large datasets.

## Example code

```
PUT /my_index
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 2
  }
}
```
## Output example

```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my_index"
}
```

The code above creates an index named "my_index" with 3 primary shards and 2 replicas. The "number_of_shards" setting specifies the number of primary shards to create in the index, while the "number_of_replicas" setting specifies the number of replica shards to create.

Elasticsearch can be used for a variety of tasks, such as logging, full-text search, analytics, and data storage. It can be used to search large datasets quickly, and to analyze data with aggregations and analytics.

## Helpful links

- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Elasticsearch Tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)

onelinerhub: [What is Elasticsearch and how is it used?](https://onelinerhub.com/elasticsearch/what-is-elasticsearch-and-how-is-it-used)