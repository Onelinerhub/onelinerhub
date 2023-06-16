# indexing

How do I bulk index documents in Elasticsearch?
// plain

Indexing documents in Elasticsearch can be done using the Bulk API. This API allows for multiple documents to be indexed in a single request. To bulk index documents, you need to create a request body containing the documents to be indexed. This request body should be formatted in the JSON format.

Below is an example of a request body for bulk indexing documents:

```
{ "index" : { "_index" : "my_index", "_type" : "_doc" } }
{ "title" : "My Document", "body" : "This is the body of my document" }
{ "index" : { "_index" : "my_index", "_type" : "_doc" } }
{ "title" : "My Second Document", "body" : "This is the body of my second document" }
```

This request body contains two documents to be indexed in the index "my_index". Each document is preceded by a JSON object containing the index and type of the document.

Once the request body is created, you can send it to Elasticsearch using the Bulk API. The API endpoint for this is `_bulk`. The response will contain the results of the indexing operation, including any errors that occurred.

Parts of the example code:

* `{ "index" : { "_index" : "my_index", "_type" : "_doc" } }` - This is the JSON object that defines the index and type for the document.
* `{ "title" : "My Document", "body" : "This is the body of my document" }` - This is the JSON object containing the document to be indexed.
* `_bulk` - This is the API endpoint for the Bulk API.

## Helpful links

* [Elasticsearch Bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html)
* [JSON Formatting](https://www.json.org/)

onelinerhub: [indexing

How do I bulk index documents in Elasticsearch?](https://onelinerhub.com/elasticsearch/indexing--how-do-i-bulk-index-documents-in-elasticsearch)