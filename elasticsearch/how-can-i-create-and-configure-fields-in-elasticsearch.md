# How can I create and configure fields in Elasticsearch?
// plain

Creating and configuring fields in Elasticsearch can be done with the `PUT` mapping API. This API allows you to define the data type for each field, as well as define any custom analyzers or tokenizers to be used.

## Example code

```
PUT my_index
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      },
      "description": {
        "type": "text",
        "analyzer": "english"
      }
    }
  }
}
```

## Output example

```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my_index"
}
```

In the example code, two fields are created: `title` and `description`. The `title` field is of type `text`, while the `description` field is of type `text` and uses the `english` analyzer.

## Code explanation


1. `PUT my_index` - specifies the name of the index to create or update.
2. `"mappings": {` - begins the mappings section of the API.
3. `"properties": {` - begins the properties section of the mappings.
4. `"title": {` - begins the definition of the `title` field.
5. `"type": "text"` - sets the type of the `title` field to `text`.
6. `"description": {` - begins the definition of the `description` field.
7. `"type": "text",` - sets the type of the `description` field to `text`.
8. `"analyzer": "english"` - sets the analyzer for the `description` field to `english`.

## Helpful links

- [Elasticsearch Mapping API Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)
- [Elasticsearch Analyzers Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-analyzers.html)

onelinerhub: [How can I create and configure fields in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-create-and-configure-fields-in-elasticsearch)