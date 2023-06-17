# How can I get started with using Elasticsearch OSS?
// plain

1. First, download and install the Elasticsearch OSS from [elastic.co](https://www.elastic.co/downloads/elasticsearch).
2. Once installed, you can start up the Elasticsearch server by running `./bin/elasticsearch` from the installation directory.
3. To verify that the server is running, you can use `curl` to make a request to the server, like this:
```
$ curl -XGET 'localhost:9200'
{
  "name" : "Ludwig",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "sEjEeVXFQKqC7xj3X5c2Ng",
  "version" : {
    "number" : "7.10.2",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "f27399d",
    "build_date" : "2021-01-12T17:10:04.951332Z",
    "build_snapshot" : false,
    "lucene_version" : "8.7.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```
4. You can now use the Elasticsearch API to index documents, search, and perform other operations. For example, you can index a document like this:
```
$ curl -XPUT 'localhost:9200/blog/post/1' -H 'Content-Type: application/json' -d '
{
  "title" : "My first blog post",
  "body" : "This is my first blog post!"
}
'

{"_index":"blog","_type":"post","_id":"1","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```
5. You can then search for documents using the Elasticsearch query DSL, like this:
```
$ curl -XGET 'localhost:9200/blog/post/_search?q=blog'
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.2876821,
    "hits" : [
      {
        "_index" : "blog",
        "_type" : "post",
        "_id" : "1",
        "_score" : 0.2876821,
        "_source" : {
          "title" : "My first blog post",
          "body" : "This is my first blog post!"
        }
      }
    ]
  }
}
```
6. To learn more about the Elasticsearch API and query DSL, you can refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).
7. You can also explore the [Elasticsearch Tutorials](https://www.elastic.co/tutorials) to get started with more advanced features.

onelinerhub: [How can I get started with using Elasticsearch OSS?](https://onelinerhub.com/elasticsearch/how-can-i-get-started-with-using-elasticsearch-oss)