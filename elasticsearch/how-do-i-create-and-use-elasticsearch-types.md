# How do I create and use Elasticsearch types?
// plain

Creating and using Elasticsearch types is a straightforward process.

1. First, create an index in Elasticsearch. This can be done with the following command:
```
PUT /my_index
```

2. Next, create a type within this index. This can be done with the following command:
```
PUT /my_index/my_type
```

3. Then, add a document to the type. This can be done with the following command:
```
PUT /my_index/my_type/1
{
  "name": "John Doe"
}
```

4. Finally, query the document. This can be done with the following command:
```
GET /my_index/my_type/1
```
The output should be the document that was added in the previous step:
```
{
  "_index": "my_index",
  "_type": "my_type",
  "_id": "1",
  "_version": 1,
  "found": true,
  "_source": {
    "name": "John Doe"
  }
}
```

In summary, Elasticsearch types can be created and used by:
1. Creating an index in Elasticsearch
2. Creating a type within the index
3. Adding a document to the type
4. Querying the document

## Helpful links
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Elasticsearch REST API Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs.html)

onelinerhub: [How do I create and use Elasticsearch types?](https://onelinerhub.com/elasticsearch/how-do-i-create-and-use-elasticsearch-types)