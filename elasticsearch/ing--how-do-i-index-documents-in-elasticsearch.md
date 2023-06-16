# ing

How do I index documents in Elasticsearch?
// plain

Elasticsearch provides a powerful and easy-to-use API for indexing documents. To index a document in Elasticsearch, you must first create an index and specify the type of document you are indexing. You can then use the index API to add the document to the index. Here is an example of how to index a document using the Elasticsearch API:

```
POST /my_index/my_type/1
{
    "title": "My Document",
    "body": "This is my document"
}
```

This example will index a document with the title "My Document" and the body "This is my document" in the index "my_index" with the type "my_type".

The index API can also be used to update existing documents. To update a document, you must specify the ID of the document you want to update. Here is an example of how to update a document using the Elasticsearch API:

```
PUT /my_index/my_type/1
{
    "title": "My Updated Document",
    "body": "This is my updated document"
}
```

This example will update the document with the ID 1 in the index "my_index" with the type "my_type" to have the title "My Updated Document" and the body "This is my updated document".

You can also delete documents with the delete API. Here is an example of how to delete a document using the Elasticsearch API:

```
DELETE /my_index/my_type/1
```

This example will delete the document with the ID 1 in the index "my_index" with the type "my_type".

## Helpful links

- [Elasticsearch Index API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html)
- [Elasticsearch Update API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-update.html)
- [Elasticsearch Delete API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-delete.html)

onelinerhub: [ing

How do I index documents in Elasticsearch?](https://onelinerhub.com/elasticsearch/ing--how-do-i-index-documents-in-elasticsearch)