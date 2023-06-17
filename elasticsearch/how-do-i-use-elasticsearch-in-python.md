# How do I use elasticsearch in Python?
// plain

Elasticsearch is a distributed, open source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. Python can be used to interact with Elasticsearch through the Elasticsearch Python client.

To use Elasticsearch with Python, first install the Elasticsearch Python client library using pip:

```
pip install elasticsearch
```

Then, import the client library and create an instance of the Elasticsearch client:

```
from elasticsearch import Elasticsearch

es = Elasticsearch()
```

Using the client, you can perform various operations such as indexing, searching, and deleting documents. For example, you can index a document like this:

```
es.index(index='my_index', doc_type='test', id=1, body={'name': 'John Doe'})
```

This will index the document with the given `index` and `doc_type`, and assign it the ID `1`. The `body` parameter contains the content of the document.

You can then search for the document using the `search()` method:

```
res = es.search(index='my_index', body={'query': {'match_all': {}}})
print(res)
```

This will return the document that was indexed earlier:

```
{'took': 2, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 1.0, 'hits': [{'_index': 'my_index', '_type': 'test', '_id': '1', '_score': 1.0, '_source': {'name': 'John Doe'}}]}}
```

The Elasticsearch Python client also allows you to delete documents, update documents, and perform various other operations you can find in the [official documentation](https://elasticsearch-py.readthedocs.io/en/master/).

## Code explanation
**

- `pip install elasticsearch`: This command installs the Elasticsearch Python client library.
- `from elasticsearch import Elasticsearch`: This imports the Elasticsearch client library.
- `es = Elasticsearch()`: This creates an instance of the Elasticsearch client.
- `es.index(index='my_index', doc_type='test', id=1, body={'name': 'John Doe'})`: This indexes a document with the given `index` and `doc_type`, and assigns it the ID `1`. The `body` parameter contains the content of the document.
- `res = es.search(index='my_index', body={'query': {'match_all': {}}})`: This searches for the document that was indexed earlier.
- `print(res)`: This prints the document that was returned by the search.

onelinerhub: [How do I use elasticsearch in Python?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-in-python)