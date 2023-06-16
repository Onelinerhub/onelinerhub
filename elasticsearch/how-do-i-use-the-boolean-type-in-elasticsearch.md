# How do I use the boolean type in Elasticsearch?
// plain

The boolean type in Elasticsearch is used to store boolean values, which are either true or false. To use the boolean type, you must first define a mapping for a field that specifies the boolean type. For example, to define a mapping for a field called "is_active":

```
PUT my_index
{
  "mappings": {
    "properties": {
      "is_active": {
        "type": "boolean"
      }
    }
  }
}
```

Once the mapping is defined, you can add documents to the index with boolean values. For example, to add a document with the "is_active" field set to true:

```
PUT my_index/_doc/1
{
  "is_active": true
}
```

You can then query the index using boolean queries. For example, to query for all documents with the "is_active" field set to true:

```
GET my_index/_search
{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "is_active": true
        }
      }
    }
  }
}
```

This will return all documents with the "is_active" field set to true.

- **Mapping Definition**: This defines the mapping for the field, specifying the boolean type.
- **Adding Documents**: This adds a document with the "is_active" field set to true.
- **Querying the Index**: This queries the index using boolean queries to return all documents with the "is_active" field set to true.

## Helpful links
- [Boolean Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/boolean.html)
- [Adding Documents](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html)
- [Querying the Index](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html)

onelinerhub: [How do I use the boolean type in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-use-the-boolean-type-in-elasticsearch)