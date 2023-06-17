# How do I remove an index in Elasticsearch?
// plain

To remove an index in Elasticsearch, you can use the `DELETE` API. The syntax for this API is as follows:

```
DELETE /<index_name>
```

Where `<index_name>` is the name of the index you want to delete.

For example, if you want to delete an index called `my_index`, you can use the following command:

```
DELETE /my_index
```

This will delete the index `my_index` from your Elasticsearch instance.

The parts of the command are as follows:

* `DELETE` - the HTTP method used to delete the index
* `/my_index` - the name of the index to be deleted

For more information, please see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-delete-index.html).

onelinerhub: [How do I remove an index in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-remove-an-index-in-elasticsearch)