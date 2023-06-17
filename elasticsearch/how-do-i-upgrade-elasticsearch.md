# How do I upgrade Elasticsearch?
// plain

1. To upgrade Elasticsearch, you first need to download the latest version from the [Elasticsearch Download Page](https://www.elastic.co/downloads/elasticsearch).

2. Once you have the latest version downloaded, you can use the `elasticsearch-plugin` command to install it. For example:

```
$ elasticsearch-plugin install file:/path/to/elasticsearch-x.x.x.zip
```

3. After the installation is complete, the output should be similar to this:

```
-> Installing file:/path/to/elasticsearch-x.x.x.zip
-> Downloading
.............................................................................................DONE
-> Installed file:/path/to/elasticsearch-x.x.x.zip into /usr/share/elasticsearch/plugins/x.x.x
```

4. After the installation is complete, you need to restart the Elasticsearch service for the changes to take effect. You can use the following command to do that:

```
$ sudo service elasticsearch restart
```

5. After the service is restarted, you can check the version of Elasticsearch by running the following command:

```
$ curl -XGET 'localhost:9200'
```

6. The output should be similar to this:

```
{
  "name" : "node-1",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "abcdefghijklmnopqrstuvwxyz",
  "version" : {
    "number" : "x.x.x",
    "build_hash" : "abcdefghijklmnopqrstuvwxyz",
    "build_date" : "YYYY-MM-DDTHH:mm:ss.zzzZ",
    "build_snapshot" : false,
    "lucene_version" : "x.x.x"
  },
  "tagline" : "You Know, for Search"
}
```

7. If the version number in the output matches the version you installed, then your upgrade was successful.

onelinerhub: [How do I upgrade Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-upgrade-elasticsearch)