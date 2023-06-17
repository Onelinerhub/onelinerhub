# How can I use an elasticsearch viewer to view my data?
// plain

An elasticsearch viewer is a tool that allows you to view data stored in an elasticsearch cluster. It can be used to query and visualize data stored in an elasticsearch index.

For example, to query for all documents in an index, you can use the following code:
```
GET /_search
```
The output of this query will be a list of documents and associated metadata.

The viewer can also be used to visualize data stored in an elasticsearch index. For example, to generate a pie chart of the number of documents in an index, you can use the following code:
```
GET /_search
{
  "aggs": {
    "document_count": {
      "terms": {
        "field": "_index"
      }
    }
  }
}
```
This query will generate a pie chart of the number of documents in each index.

In addition to querying and visualizing data stored in an elasticsearch index, the elasticsearch viewer can also be used to monitor the performance of the cluster. For example, to view the cluster health, you can use the following code:
```
GET /_cluster/health
```
The output of this query will be a JSON object containing the cluster health information.

## Helpful links
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Elasticsearch Viewer Tutorial](https://www.elastic.co/blog/getting-started-with-the-elasticsearch-viewer)

onelinerhub: [How can I use an elasticsearch viewer to view my data?](https://onelinerhub.com/elasticsearch/how-can-i-use-an-elasticsearch-viewer-to-view-my-data)