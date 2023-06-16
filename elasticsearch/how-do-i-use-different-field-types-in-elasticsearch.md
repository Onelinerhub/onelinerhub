# How do I use different field types in Elasticsearch?
// plain

To use different field types in Elasticsearch, you need to specify the type when creating an index or mapping. For example, to create a mapping for a field of type keyword, you could use the following code:

```
PUT my_index
{
  "mappings": {
    "properties": {
      "my_field": {
        "type":  "keyword"
      }
    }
  }
}
```

The output of this code would be:
```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my_index"
}
```

The following is a list of the available field types in Elasticsearch, with a brief explanation of each:
* **text**: used to store string values that will be analyzed for full-text search.
* **keyword**: used to store non-analyzed string values for exact matching.
* **date**: used to store date values.
* **long**: used to store 64-bit integer values.
* **double**: used to store double-precision 64-bit floating point values.
* **boolean**: used to store boolean values.
* **object**: used to store complex objects as nested documents.
* **nested**: used to store arrays of complex objects as nested documents.

For more information, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html).

onelinerhub: [How do I use different field types in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-use-different-field-types-in-elasticsearch)