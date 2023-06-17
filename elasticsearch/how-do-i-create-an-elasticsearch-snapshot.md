# How do I create an Elasticsearch snapshot?
// plain

Creating an Elasticsearch snapshot is a two-step process:

1. Create a Repository:

A repository is a location where snapshots are stored. To create a repository, use the `PUT` API with the repository name as a parameter. The following example creates a repository named `my_backup`:

```
PUT _snapshot/my_backup
{
  "type": "fs",
  "settings": {
    "location": "/mnt/my_backup"
  }
}
```

2. Create a Snapshot:

Once the repository is created, snapshots can be taken. To create a snapshot, use the `PUT` API with the repository name and snapshot name as parameters. The following example creates a snapshot named `my_snapshot` in the `my_backup` repository:

```
PUT _snapshot/my_backup/my_snapshot
```

The snapshot will be created in the repository location (`/mnt/my_backup` in this example) and can be used for restoring the cluster.

For more information, see [Elasticsearch Snapshots](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-snapshots.html) and [Snapshot and Restore](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-snapshots.html#_snapshot).

onelinerhub: [How do I create an Elasticsearch snapshot?](https://onelinerhub.com/elasticsearch/how-do-i-create-an-elasticsearch-snapshot)