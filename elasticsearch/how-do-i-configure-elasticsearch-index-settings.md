# How do I configure Elasticsearch index settings?
// plain

1. To configure Elasticsearch index settings, you need to use the `PUT` API.
2. For example, to set the number of shards for an index, you can use the following `PUT` request:

```
PUT /my_index
{
  "settings" : {
    "index" : {
      "number_of_shards" : 3
    }
  }
}
```

3. The response of the request will be a `200 OK` status code if the settings were successfully changed.
4. You can also set other settings such as the number of replicas, the refresh interval, the maximum number of documents, etc.
5. You can find more information about the available settings and their parameters in the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules.html).
6. Additionally, you can use the `GET` API to retrieve the current settings for an index.
7. For example, the following `GET` request will return the current settings for an index:

```
GET /my_index/_settings
```

The response of the request will be a `200 OK` status code and a JSON object containing the current settings for the index.

onelinerhub: [How do I configure Elasticsearch index settings?](https://onelinerhub.com/elasticsearch/how-do-i-configure-elasticsearch-index-settings)