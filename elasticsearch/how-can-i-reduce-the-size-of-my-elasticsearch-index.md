# How can I reduce the size of my Elasticsearch index?
// plain

1. Use **fielddata** parameter to reduce the size of your Elasticsearch index. Fielddata allows you to store the values of certain fields in memory, which can reduce the size of your index.

2. Use **_source** field to reduce the size of your Elasticsearch index. By default, Elasticsearch stores the original document in the _source field. You can disable this by setting the “_source” field to false.

3. Use **index.store.compress** setting to reduce the size of your Elasticsearch index. This setting allows you to compress the data stored in your index.

4. Use **_field_names** field to reduce the size of your Elasticsearch index. The _field_names field stores the names of all the fields in your index. You can disable this field by setting the “_field_names” field to false.

5. Use **_all** field to reduce the size of your Elasticsearch index. The _all field stores the values of all the fields in your index. You can disable this field by setting the “_all” field to false.

6. Use **_timestamp** field to reduce the size of your Elasticsearch index. The _timestamp field stores the date and time when the document was indexed. You can disable this field by setting the “_timestamp” field to false.

7. Use **index.refresh_interval** setting to reduce the size of your Elasticsearch index. This setting allows you to control how often the index is refreshed. A higher refresh interval will reduce the size of your index.

```
PUT my_index
{
  "settings": {
    "index.store.compress": true,
    "index.refresh_interval": "60s"
  },
  "mappings": {
    "_source": {
      "enabled": false
    },
    "_all": {
      "enabled": false
    },
    "_field_names": {
      "enabled": false
    },
    "_timestamp": {
      "enabled": false
    }
  }
}
```

No output.

onelinerhub: [How can I reduce the size of my Elasticsearch index?](https://onelinerhub.com/elasticsearch/how-can-i-reduce-the-size-of-my-elasticsearch-index)