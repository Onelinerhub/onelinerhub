# How do I upgrade to the latest version of Elasticsearch?
// plain

1. To upgrade to the latest version of Elasticsearch, you must first download the appropriate version of the software from the [Elasticsearch download page](https://www.elastic.co/downloads/elasticsearch).

2. Once the download is complete, you can install the software either manually or using a package manager such as [Homebrew](https://brew.sh/).

3. To manually install, you can extract the archive and run the following command to install the software:
```
bin/elasticsearch-plugin install <plugin-name>
```

4. After installation is complete, you need to configure the Elasticsearch instance. This can be done by editing the `elasticsearch.yml` configuration file.

5. Once the configuration is complete, you can start the Elasticsearch instance by running the following command:
```
bin/elasticsearch
```

6. After the instance is running, you can check the version of Elasticsearch by running the following command:
```
curl -XGET localhost:9200
```

7. The output should include a version field which displays the version of Elasticsearch that is running.

```
{
  "name" : "elasticsearch-node",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "I1ZqD1q8RV6VX2-sjGKG8Q",
  "version" : {
    "number" : "7.8.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "1a2f265",
    "build_date" : "2020-07-20T05:20:23.084789Z",
    "build_snapshot" : false,
    "lucene_version" : "8.5.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

onelinerhub: [How do I upgrade to the latest version of Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-upgrade-to-the-latest-version-of-elasticsearch)