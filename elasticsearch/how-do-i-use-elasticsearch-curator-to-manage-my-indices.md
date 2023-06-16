# How do I use Elasticsearch Curator to manage my indices?
// plain

Elasticsearch Curator is a powerful tool for managing indices. It allows you to define rules and policies to automate the management of your indices. To use Curator, you first need to install it.

Once installed, you can use Curator to manage your indices. For example, you can use it to delete old indices, close indices, optimize indices, or snapshot indices.

Here is an example of using Curator to delete old indices:

```
curator delete --prefix logstash- --older-than 30
```

The above command will delete all indices with a prefix of `logstash-` that are older than 30 days.

You can also use Curator to perform other operations such as closing indices, optimizing indices, or snapshotting indices.

Here is an example of using Curator to snapshot an index:

```
curator snapshot --repository my_backup --name "my_snapshot" logstash-2017.04.09
```

The above command will create a snapshot called `my_snapshot` in the repository `my_backup` for the index `logstash-2017.04.09`.

For more information on using Curator, please refer to the [official documentation](https://www.elastic.co/guide/en/elasticsearch/client/curator/current/index.html).

onelinerhub: [How do I use Elasticsearch Curator to manage my indices?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-curator-to-manage-my-indices)