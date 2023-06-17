# How do I update documents in Elasticsearch using the update by query API?
// plain

The update by query API allows you to update one or more documents in an Elasticsearch index without having to reindex the entire data set. To do this, you must specify a query that identifies the documents you want to update, and a script that contains the operations you want to perform on those documents.

For example, the following code will update all documents in the `my_index` index that have a `name` field equal to `John`:
```
POST my_index/_update_by_query
{
  "query": {
    "term": {
      "name": "John"
    }
  },
  "script": {
    "source": "ctx._source.name = params.name",
    "params": {
      "name": "John Doe"
    }
  }
}
```
This will update the `name` field of all documents matching the query to `John Doe`.

In addition to the `query` and `script` parameters, the update by query API also supports other parameters such as `conflicts`, `refresh`, and `timeout`. These parameters can be used to control how the update is performed and how it affects other operations on the index.

The update by query API is a powerful tool for making bulk updates to documents in an Elasticsearch index. For more information, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-update-by-query.html).

onelinerhub: [How do I update documents in Elasticsearch using the update by query API?](https://onelinerhub.com/elasticsearch/how-do-i-update-documents-in-elasticsearch-using-the-update-by-query-api)