# How do I index a JSON document in Elasticsearch?
// plain

In order to index a JSON document in Elasticsearch, you must first create an index, which is a logical namespace that points to one or more primary shards and can have zero or more replica shards. To create an index, you can use the `PUT` API. For example, the following command creates an index named "my_index":

```
PUT my_index
```

Once the index is created, you can index a JSON document into it by using the `POST` API. For example, the following command indexes a document with ID 1 into the index "my_index":

```
POST my_index/_doc/1
{
  "name": "John Doe",
  "age": 34
}
```

The following is the output of the above command:

```
{
  "_index": "my_index",
  "_type": "_doc",
  "_id": "1",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 1
}
```

The parts of the code are:
- `PUT my_index`: creates an index named "my_index"
- `POST my_index/_doc/1`: indexes a document with ID 1 into the index "my_index"
- `{ "name": "John Doe", "age": 34 }`: the JSON document to be indexed

## Helpful links
- [Index API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html)
- [JSON Data Types](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html)

onelinerhub: [How do I index a JSON document in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-index-a-json-document-in-elasticsearch)