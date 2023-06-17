# How do I use Elasticsearch with Python?
// plain

Using Elasticsearch with Python is easy and straightforward. The [`elasticsearch-py`](https://github.com/elastic/elasticsearch-py) client library can be used to interface with an Elasticsearch cluster. The library provides a convenient Python API to access the cluster's indices and documents.

To get started, install the `elasticsearch` package using `pip`:

```
pip install elasticsearch
```

Once the package is installed, you can use it to connect to an Elasticsearch cluster:

```python
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
```

Once the connection is established, you can use the `es` object to interact with the cluster. For example, to list all indices in the cluster:

```python
es.indices.get_alias("*")
```

The output of the above command could look like this:

```
{
    'index-1': {},
    'index-2': {},
    'index-3': {}
}
```

You can also use the `es` object to create, update and delete documents in the cluster's indices. For example, to index a document:

```python
doc = {
    'name': 'John Doe',
    'age': 33
}

es.index(index='users', doc_type='_doc', id=1, body=doc)
```

You can find more information about using `elasticsearch-py` in the [official documentation](https://elasticsearch-py.readthedocs.io/en/master/).

onelinerhub: [How do I use Elasticsearch with Python?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-with-python)