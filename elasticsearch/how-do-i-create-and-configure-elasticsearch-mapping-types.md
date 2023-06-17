# How do I create and configure elasticsearch mapping types?
// plain

To create and configure elasticsearch mapping types, you need to first define the mapping type by making a `PUT` request to the `_mapping` endpoint. For example, you can use the following code to create a mapping type for a `users` index:

```
PUT /users/_mapping
{
  "properties": {
    "name": {
      "type": "text"
    }
  }
}
```

The output of the above code should be `{"acknowledged":true}`. This indicates that the mapping type was successfully created.

Next, you can configure the mapping type by adding more properties to it. For example, you can add an `age` property to the `users` mapping type:

```
PUT /users/_mapping
{
  "properties": {
    "name": {
      "type": "text"
    },
    "age": {
      "type": "integer"
    }
  }
}
```

The output of the above code should be `{"acknowledged":true}`. This indicates that the mapping type was successfully configured.

You can add more properties and configure the mapping type as needed.

## Helpful links
- [Elasticsearch Mapping Types](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)
- [Elasticsearch Mapping API](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-api.html)

onelinerhub: [How do I create and configure elasticsearch mapping types?](https://onelinerhub.com/elasticsearch/how-do-i-create-and-configure-elasticsearch-mapping-types)