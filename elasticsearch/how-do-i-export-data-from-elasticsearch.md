# How do I export data from Elasticsearch?
// plain

To export data from Elasticsearch, you can use the [Elasticsearch _export API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-export.html). This API allows you to export the contents of an index in bulk.

For example, to export all data from an index called "my_index" using the `_export` API, you can use the following command:
```
curl -X POST "localhost:9200/my_index/_export?pretty"
```

The output of this command will look something like this:
```
{
  "took" : 0,
  "timed_out" : false,
  "_scroll_id" : "DnF1ZXJ5VGhlbkZldGNoBQAAAAAAAAGtOExXbVV3V0l5YXVmRVV4M0t4TnA3V2xnQQ==",
  "exported_documents" : 0,
  "total_exported_documents" : 0,
  "batches" : 0
}
```

The `_export` API supports a variety of parameters, such as `scroll`, `search_type`, `fields`, `size`, and `sort`. These parameters can be used to customize the export process, such as limiting the number of documents returned, or sorting the documents before exporting.

For more information on the `_export` API and its parameters, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-export.html).

onelinerhub: [How do I export data from Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-export-data-from-elasticsearch)