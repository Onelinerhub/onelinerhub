# How do I create an Elasticsearch mapping?
// plain

To create an Elasticsearch mapping, you need to define the structure of your data in a JSON document. This document is then sent to the Elasticsearch server via an API call.

The following example code demonstrates how to create a mapping for an index called `my_index`:
```
PUT my_index
{
  "mappings": {
    "properties": {
      "user": {
        "type": "keyword"
      },
      "message": {
        "type": "text"
      }
    }
  }
}
```
The output of the above code will be a `200 OK` response.

The code consists of the following parts:
1. `PUT my_index`: This is the API call to create the index.
2. `mappings`: This is the key that holds the mapping definition.
3. `properties`: This is the key that holds the field definitions.
4. `user` and `message`: These are the field names.
5. `type`: This is the data type of the field.

For more information on creating mappings in Elasticsearch, please refer to the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html).

onelinerhub: [How do I create an Elasticsearch mapping?](https://onelinerhub.com/elasticsearch/how-do-i-create-an-elasticsearch-mapping)