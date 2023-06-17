# How can I use Python to access data stored in Elasticsearch?
// plain

You can use the official Python client for Elasticsearch, [`elasticsearch-py`](https://elasticsearch-py.readthedocs.io/en/master/), to access data stored in Elasticsearch. Here is an example of how to connect to an Elasticsearch cluster and query it using `elasticsearch-py`:

```python
from elasticsearch import Elasticsearch

# Connect to the Elasticsearch cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Query the cluster
res = es.search(index="my_index", body={"query": {"match_all": {}}})

# Print the response
print(res)
```

## Output example

```
{'took': 5,
 'timed_out': False,
 '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0},
 'hits': {'total': {'value': 4, 'relation': 'eq'},
  'max_score': 1.0,
  'hits': [{'_index': 'my_index',
    '_type': '_doc',
    '_id': '1',
    '_score': 1.0,
    '_source': {'field1': 'value1', 'field2': 'value2'}},
   {'_index': 'my_index',
    '_type': '_doc',
    '_id': '2',
    '_score': 1.0,
    '_source': {'field1': 'value3', 'field2': 'value4'}},
   {'_index': 'my_index',
    '_type': '_doc',
    '_id': '3',
    '_score': 1.0,
    '_source': {'field1': 'value5', 'field2': 'value6'}},
   {'_index': 'my_index',
    '_type': '_doc',
    '_id': '4',
    '_score': 1.0,
    '_source': {'field1': 'value7', 'field2': 'value8'}}]}}
```

The code above does the following:
1. Imports the `elasticsearch` module from `elasticsearch-py`.
2. Connects to an Elasticsearch cluster using the `Elasticsearch` class.
3. Queries the cluster using the `search()` method.
4. Prints the response from the query.

For more information, see the [`elasticsearch-py` documentation](https://elasticsearch-py.readthedocs.io/en/master/).

onelinerhub: [How can I use Python to access data stored in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-python-to-access-data-stored-in-elasticsearch)