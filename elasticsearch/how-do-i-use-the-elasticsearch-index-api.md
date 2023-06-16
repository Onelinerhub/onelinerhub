# How do I use the Elasticsearch Index API?
// plain

The Elasticsearch Index API allows you to add, update, or delete documents from an Elasticsearch index. Here is an example of how to use the Index API with Python:

```
# Import the Elasticsearch client library
from elasticsearch import Elasticsearch

# Connect to the Elasticsearch cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Index a document
es.index(index='my-index', doc_type='test', id=1, body={'name': 'John Doe'})
```

This code will index a document with an id of 1 and a name of "John Doe" into the "my-index" index.

You can also use the Index API to update or delete documents. To update a document, you will need to use the `update()` method, passing in the index, doc_type, id, and body containing the updated fields:

```
es.update(index='my-index', doc_type='test', id=1, body={'doc': {'name': 'Jane Doe'}})
```

This code will update the document with an id of 1 in the "my-index" index, setting the name field to "Jane Doe".

To delete a document, you will need to use the `delete()` method, passing in the index, doc_type, and id of the document:

```
es.delete(index='my-index', doc_type='test', id=1)
```

This code will delete the document with an id of 1 in the "my-index" index.

## Helpful links

- [Elasticsearch Documentation: Index API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html)
- [Elasticsearch Client Library Documentation](https://elasticsearch-py.readthedocs.io/en/master/)

onelinerhub: [How do I use the Elasticsearch Index API?](https://onelinerhub.com/elasticsearch/how-do-i-use-the-elasticsearch-index-api)