# How do I get the version of Elasticsearch I am using?
// plain

To get the version of the Elasticsearch you are using, you can use the `cat` API. This API allows you to retrieve the version information about the Elasticsearch instance.

## Example


```
curl -XGET 'localhost:9200'
```

## Output example

```
{
  "name" : "elasticsearch-node",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "v-HlwfvVQbq7KjE_zVfQ",
  "version" : {
    "number" : "7.3.2",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "e9ccaed468e2fac2275a3761849cbee64b39519f",
    "build_date" : "2019-09-06T14:40:30.409026Z",
    "build_snapshot" : false,
    "lucene_version" : "8.2.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

In the output, the version of the Elasticsearch instance is `7.3.2`.

## Code explanation

1. `curl -XGET 'localhost:9200'` - Retrieves the version information about the Elasticsearch instance.

## Helpful links
1. [Elasticsearch - Get API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-get.html)

onelinerhub: [How do I get the version of Elasticsearch I am using?](https://onelinerhub.com/elasticsearch/how-do-i-get-the-version-of-elasticsearch-i-am-using)