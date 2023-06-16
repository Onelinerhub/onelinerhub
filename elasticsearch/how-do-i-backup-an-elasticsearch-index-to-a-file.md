# How do I backup an Elasticsearch index to a file?
// plain

Using the Elasticsearch snapshot and restore API, you can easily backup an Elasticsearch index to a file. The snapshot API allows you to take a backup of a cluster, a single index, or even multiple indices.

For example, to backup an index named `my-index` to a file, you can use the following API call:

```
PUT /_snapshot/my-backup/my-index-backup?wait_for_completion=true
{
  "indices": "my-index"
}
```

This will create a snapshot named `my-index-backup` in the repository `my-backup`. The `wait_for_completion` parameter ensures that the API call will wait until the snapshot is completed before returning.

To restore the index, you can use the following API call:

```
POST /_snapshot/my-backup/my-index-backup/_restore
```

This will restore the snapshot `my-index-backup` from the repository `my-backup`.

## Helpful links
* [Elasticsearch Snapshot and Restore API](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-snapshots.html)
* [Elasticsearch Snapshot and Restore API Examples](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-snapshots-examples.html)

onelinerhub: [How do I backup an Elasticsearch index to a file?](https://onelinerhub.com/elasticsearch/how-do-i-backup-an-elasticsearch-index-to-a-file)