# How can users get started with Elasticsearch?
// plain

1. First, users need to [download and install](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) Elasticsearch on their system.
2. Once installed, users can start an instance of Elasticsearch by running the following command in the terminal:
```
$ bin/elasticsearch
```
3. After starting the instance, users can verify that it is running by making a HTTP request to the cluster using curl:
```
$ curl -X GET "localhost:9200"

## Output example

{
  "name" : "Gwendolyn",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "mXo_b7-VQm-2E9TKXe9h3g",
  "version" : {
    "number" : "7.3.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "ef48eb35cf30adf4db14086e8aabd07ef6fb113f",
    "build_date" : "2019-07-24T19:35:50.547737Z",
    "build_snapshot" : false,
    "lucene_version" : "8.1.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

4. The output shows that the instance is running and provides information about the version of Elasticsearch.
5. After verifying the instance is running, users can begin to index data into Elasticsearch. To do this, users need to send a `POST` request with the data they want to index as the body of the request. For example:
```
$ curl -X POST "localhost:9200/customer/external" -H 'Content-Type: application/json' -d'
{
  "name": "John Doe"
}
'

## Output example

{
  "_index" : "customer",
  "_type" : "external",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

6. The output shows that the document was created successfully.
7. For more information on getting started with Elasticsearch, users can check out the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html).

onelinerhub: [How can users get started with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-users-get-started-with-elasticsearch)