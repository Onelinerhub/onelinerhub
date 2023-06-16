# How do I retrieve a document by its ID using Elasticsearch?
// plain

Retrieving a document by its ID using Elasticsearch is fairly straightforward. You can use the `get` API to fetch a document by its ID.

For example, if you have an index called `my_index` and a type called `my_type`, and the document has an ID of `1`, you can use the following code to retrieve the document:

```
GET my_index/my_type/1
```

The output of this code should be a JSON object containing the document data.

The code can be broken down into the following parts:
- `GET`: This is the HTTP verb used to retrieve a document.
- `my_index`: This is the name of the index.
- `my_type`: This is the type of the document.
- `1`: This is the ID of the document.

For more information, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-get.html).

onelinerhub: [How do I retrieve a document by its ID using Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-retrieve-a-document-by-its-id-using-elasticsearch)