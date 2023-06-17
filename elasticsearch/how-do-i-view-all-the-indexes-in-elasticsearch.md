# How do I view all the indexes in Elasticsearch?
// plain

To view all the indexes in Elasticsearch, you can use the `_cat/indices` API. This API returns a list of all the existing indexes in an Elasticsearch cluster. For example:

```
GET /_cat/indices?v
```

The output of this API will be something like this:

```
health status index               uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   index1              k1eR7UZ0R9C7h2t2vY_JQg   5   1       1000            0     5.3mb          5.3mb
yellow open   index2              9VrVVmV6RjmVJy_5L2hKPQ   5   1        500            0     2.6mb          2.6mb
```

The parts of this code are:
- `GET`: The type of request we are making to the API.
- `/_cat/indices`: The API endpoint we are calling.
- `?v`: An optional parameter that specifies that we want the API to return verbose output.

For more information about the `_cat/indices` API, you can refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html).

onelinerhub: [How do I view all the indexes in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-view-all-the-indexes-in-elasticsearch)