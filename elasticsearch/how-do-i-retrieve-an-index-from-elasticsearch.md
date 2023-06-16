# How do I retrieve an index from Elasticsearch?
// plain

Retrieving an index from Elasticsearch can be done using the _get_ index API. This API allows you to retrieve the mapping, settings, and index aliases for one or more indices.

## Example code

```
GET /my_index
```

This request will return the mappings, settings, and index aliases for the `my_index` index.

The response will contain the following parts:

1. `acknowledged` - a boolean indicating if the request was successful
2. `index` - the name of the index
3. `mappings` - the mappings for the index
4. `settings` - the settings for the index
5. `aliases` - the aliases for the index

```
{
    "acknowledged": true,
    "index": "my_index",
    "mappings": {...},
    "settings": {...},
    "aliases": {...}
}
```

For more information, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-get-index.html).

onelinerhub: [How do I retrieve an index from Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-retrieve-an-index-from-elasticsearch)