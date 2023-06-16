# How do I install Elasticsearch?
// plain

1. Download and install the latest version of Java from the [Oracle website](https://www.oracle.com/java/technologies/javase-downloads.html).

2. Download and extract the Elasticsearch zip file from the [Elastic website](https://www.elastic.co/downloads/elasticsearch).

3. Open the `config/elasticsearch.yml` file and edit the `cluster.name` and `node.name` settings.

4. Run the following command to start Elasticsearch:
```
bin/elasticsearch
```
5. Check the output of the command to make sure Elasticsearch is running without any errors.

6. To test if Elasticsearch is running, open a web browser and go to `http://localhost:9200`. You should see a JSON response with the Elasticsearch version number.

7. You can also use the `curl` command to test if Elasticsearch is running:
```
curl -X GET http://localhost:9200
```
## Output example

```
{
  "name" : "your_node_name",
  "cluster_name" : "your_cluster_name",
  "cluster_uuid" : "your_cluster_uuid",
  "version" : {
    "number" : "7.7.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "81a1e9eda8e6183f5237786246f6dced26a10eaf",
    "build_date" : "2020-05-28T16:30:01.040088Z",
    "build_snapshot" : false,
    "lucene_version" : "8.5.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

onelinerhub: [How do I install Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-install-elasticsearch)