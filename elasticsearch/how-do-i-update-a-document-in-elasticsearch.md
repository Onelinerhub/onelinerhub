# How do I update a document in Elasticsearch?
// plain

Updating a document in Elasticsearch is relatively simple. The example code below shows how to update a document using the Update API:
```
PUT my_index/_doc/1
{
  "title": "Updated title"
}
```
This will update the document with ID 1 in the my_index index, setting its title field to "Updated title".

## Code explanation


1. `PUT`: This is the HTTP verb used to make the update request.
2. `my_index`: This is the name of the index containing the document to be updated.
3. `_doc/1`: This is the type and ID of the document to be updated.
4. `"title": "Updated title"`: This is the field and value to be updated in the document.

For more information on updating documents in Elasticsearch, please refer to the [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/docs-update.html).

onelinerhub: [How do I update a document in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-update-a-document-in-elasticsearch)