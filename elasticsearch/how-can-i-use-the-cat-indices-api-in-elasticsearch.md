# How can I use the cat indices API in Elasticsearch?
// plain

The cat indices API in Elasticsearch can be used to retrieve and manage information about indices. It provides a simple way to get a list of all indices, or to filter the list to return only indices that match specific criteria.

For example, to get a list of all indices, you can use the following command:

```
GET /_cat/indices
```

The output of this command would look something like this:

```
health status index uuid pri rep docs.count docs.deleted store.size pri.store.size
green open   test_index   nE7K8l7QSVqH2X8N6KiM2w   5   1     0            0      5.2kb           5.2kb
```

Here are some of the parameters that can be used with the cat indices API:

- `h`: used to specify the fields to be returned in the output
- `v`: used to return the output in a verbose format
- `format`: used to specify the output format, such as json, yaml, or text
- `s`: used to sort the output by a specific field

For more information about the cat indices API, you can refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html).

onelinerhub: [How can I use the cat indices API in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-the-cat-indices-api-in-elasticsearch)