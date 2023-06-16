# How do I create an Elasticsearch index template?
// plain

To create an Elasticsearch index template, you need to define the index pattern and the corresponding mapping.

```
PUT _template/template_1
{
  "index_patterns": ["*"],
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "_source": {
      "enabled": true
    },
    "properties": {
      "title": {
        "type": "text"
      }
    }
  }
}
```

This example code creates a template called `template_1` that applies to all indices and sets the number of shards to 1. It also adds a mapping for a `title` field of type `text`.

The code consists of:
1. `PUT _template/template_1`: This is the request to create a template called `template_1`.
2. `index_patterns`: This is an array containing the index patterns the template should apply to. In this case, it applies to all indices (`*`).
3. `settings`: This is an object with settings that should be applied to the indices. In this example, it sets the number of shards to 1.
4. `mappings`: This is an object with the mapping for the fields in the index. In this example, it adds a mapping for a `title` field of type `text`.

For more information, see [the official Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-templates.html).

onelinerhub: [How do I create an Elasticsearch index template?](https://onelinerhub.com/elasticsearch/how-do-i-create-an-elasticsearch-index-template)