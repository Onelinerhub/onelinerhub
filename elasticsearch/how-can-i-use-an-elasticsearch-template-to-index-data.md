# How can I use an Elasticsearch template to index data?
// plain

An Elasticsearch template can be used to index data by creating a mapping that defines the fields in an index, including their data types and other indexing options. This mapping is then used to create the index when the template is applied.

For example, the following template can be used to create an index called 'test-index' with two fields, 'name' and 'age':
```
PUT _template/test-template
{
  "index_patterns": ["test-index*"],
  "mappings": {
    "properties": {
      "name": {
        "type": "text"
      },
      "age": {
        "type": "integer"
      }
    }
  }
}
```

The output of this command will be a `201 Created` response, indicating that the template has been successfully applied.

## Code explanation


1. `PUT _template/test-template` - this command creates the template, using the name `test-template`.
2. `index_patterns` - this defines the name of the index to be created when the template is applied.
3. `mappings` - this defines the fields in the index, including their data types and other indexing options.
4. `name` - this is the name of the first field in the index, with a data type of `text`.
5. `age` - this is the name of the second field in the index, with a data type of `integer`.
6. `201 Created` - this is the response indicating that the template was successfully applied.

## Helpful links

- [Elasticsearch Mapping Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)
- [Elasticsearch Template Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html)

onelinerhub: [How can I use an Elasticsearch template to index data?](https://onelinerhub.com/elasticsearch/how-can-i-use-an-elasticsearch-template-to-index-data)