# How can I use vector search in Elasticsearch?
// plain

Vector search in Elasticsearch is a powerful tool for finding documents that are similar to a given vector of values. It can be used to find similar items in a dataset, such as similar products in an e-commerce store. To use vector search in Elasticsearch, you need to create a vector field in your document mapping and store the vector values in that field.

Here is an example of how to create a vector field and store a vector of values in it:

```
PUT my_index
{
  "mappings": {
    "properties": {
      "vector_field": {
        "type": "dense_vector",
        "dims": 3
      }
    }
  }
}

PUT my_index/_doc/1
{
  "vector_field": [1.0, 2.0, 3.0]
}
```

Once the vector field has been created and the vector values stored in it, you can use the `query_string` query to search for documents that are similar to a given vector. The following example searches the `my_index` index for documents that are similar to the vector `[1.0, 2.0, 3.0]`:

```
GET my_index/_search
{
  "query": {
    "query_string": {
      "query": "vector_field: [1.0, 2.0, 3.0]"
    }
  }
}
```

If the query is successful, the output will be a list of documents that are similar to the given vector.

Parts of the example code:
- `PUT my_index`: Creates an index called `my_index`
- `type": "dense_vector"`: Sets the type of the vector field to `dense_vector`
- `dims": 3`: Sets the number of dimensions in the vector field to 3
- `PUT my_index/_doc/1`: Creates a document in the `my_index` index
- `vector_field": [1.0, 2.0, 3.0]`: Stores a vector of values in the `vector_field` field
- `GET my_index/_search`: Searches the `my_index` index for documents
- `query_string`: Uses the `query_string` query to search for documents that are similar to a given vector

## Helpful links
- [Vector fields in Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/vector.html)
- [Query string query in Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html)

onelinerhub: [How can I use vector search in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-vector-search-in-elasticsearch)