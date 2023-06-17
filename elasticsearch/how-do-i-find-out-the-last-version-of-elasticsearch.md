# How do I find out the last version of Elasticsearch?
// plain

The last version of Elasticsearch can be found on the [Elasticsearch Release Page](https://www.elastic.co/downloads/past-releases).

You can also use the [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/info-api.html) to get the last version of Elasticsearch.

## Example code


```
curl -XGET 'localhost:9200'
```

## Output example


```
{
  "name" : "elasticsearch",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "pKzTKiQOSu-7F8E3U8f6YQ",
  "version" : {
    "number" : "7.7.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "81a1e9eda8e6183f5237786246f6dced26a10eaf",
    "build_date" : "2020-05-18T14:25:17.811730Z",
    "build_snapshot" : false,
    "lucene_version" : "8.5.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

The version number of Elasticsearch can be found in the output of the command above. In this example, the last version of Elasticsearch is 7.7.1.

## Code explanation


* `curl -XGET 'localhost:9200'` - This command sends a request to the localhost on port 9200, which is the default port for Elasticsearch.

* `"number" : "7.7.1"` - This is the version number of Elasticsearch.

onelinerhub: [How do I find out the last version of Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-find-out-the-last-version-of-elasticsearch)