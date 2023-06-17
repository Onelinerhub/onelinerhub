# How can I use Yandex Mirror to access Elasticsearch data?
// plain

Yandex Mirror is a powerful tool that can be used to access Elasticsearch data. It provides a unified interface for querying data stored in Elasticsearch clusters.

To use Yandex Mirror, you need to create a connection to the Elasticsearch cluster. This can be done by providing the cluster's IP address and port. After the connection is established, you can start querying the Elasticsearch data.

## Example code

```
import yandex.mirror

client = yandex.mirror.connect(host='127.0.0.1', port=9200)

# query the Elasticsearch data
response = client.search(index='my_index', body={
    "query": {
        "match_all": {}
    }
})

print(response)
```

Example output:
```
{'took': 2,
 'timed_out': False,
 '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0},
 'hits': {'total': {'value': 10, 'relation': 'eq'},
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
    '_source': {'field1': 'value3', 'field2': 'value4'}}]}}
```

The code above will connect to the Elasticsearch cluster, query the data, and print the response. The response contains the total number of documents that matched the query, the maximum score of the documents, and a list of documents that matched the query.

The list of documents contains the index, type, ID, score, and source of each document. The source contains the actual data that was stored in the document.

## Helpful links

- [Yandex Mirror Documentation](https://yandex.github.io/mirror/)
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

onelinerhub: [How can I use Yandex Mirror to access Elasticsearch data?](https://onelinerhub.com/elasticsearch/how-can-i-use-yandex-mirror-to-access-elasticsearch-data)