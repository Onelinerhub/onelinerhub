# How do I get a list of all indexes in Elasticsearch?
// plain

To get a list of all indexes in an Elasticsearch cluster, you can use the [`cat indices` API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html). This API provides a concise summary of the health of all indices in a cluster.

## Example code

```
GET /_cat/indices?v
```

Example output:
```
health status index    uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   test1   nHG_L0e3Qz-TnVHXV3dFVQ   5   1          0            0     4.3kb         4.3kb
```

## Code explanation


- `GET`: The HTTP verb for the request.
- `/_cat/indices`: The path to the Elasticsearch endpoint for retrieving a list of indices.
- `?v`: The query parameter for verbose output.

## Helpful links

- [Elasticsearch Reference: cat indices](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html)

onelinerhub: [How do I get a list of all indexes in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-get-a-list-of-all-indexes-in-elasticsearch)