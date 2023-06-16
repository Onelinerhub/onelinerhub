# How can I check if an index exists in Elasticsearch?
// plain

You can check if an index exists in Elasticsearch using the `_cat/indices` API. For example, the following command will check if the index `myindex` exists:

```
curl -XGET 'localhost:9200/_cat/indices?v&s=index'
```

The output will be similar to this:

```
health status index               uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   myindex            d3E3Ks7qQ0yYhgT0LsV7VQ   5   1          0            0      3.3kb          3.3kb
```

The parts of the command are:

- `curl`: the command-line tool to make HTTP requests
- `-XGET`: the HTTP method to use for the request
- `localhost:9200`: the URL of the Elasticsearch instance
- `_cat/indices?v&s=index`: the API endpoint to check indices

If the index exists, it will appear in the output.

## Helpful links

- [Elasticsearch _cat API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html)
- [cURL Documentation](https://curl.haxx.se/docs/)

onelinerhub: [How can I check if an index exists in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-check-if-an-index-exists-in-elasticsearch)