# How do I install Elasticsearch on Ubuntu?
// plain

1. Download the latest version of the Elasticsearch .deb package from the [Elasticsearch website](https://www.elastic.co/downloads/elasticsearch).
2. Install the package with the following command:
```
sudo dpkg -i elasticsearch-<version>.deb
```
3. Start Elasticsearch with the following command:
```
sudo systemctl start elasticsearch.service
```
4. Verify that Elasticsearch is running by sending an HTTP request to port 9200 on localhost:
```
curl -X GET "localhost:9200"
```
## Output example

```
{
  "name" : "Q2_Ew",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "z_iQ_BVQT6GQPq_jJ-y2g",
  "version" : {
    "number" : "7.6.2",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "ef48eb35cf30adf4db14086e8aabd07ef6fb113f",
    "build_date" : "2020-03-26T06:34:37.794943Z",
    "build_snapshot" : false,
    "lucene_version" : "8.4.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```
5. To make sure Elasticsearch starts at boot time, run the following command:
```
sudo systemctl enable elasticsearch.service
```
6. To test the installation, run the following command:
```
curl -X GET "localhost:9200/_cat/health?v&pretty"
```
## Output example

```
epoch      timestamp cluster       status node.total node.data shards pri relo init unassign pending_tasks max_task_wait_time active_shards_percent
1585400389 15:03:09  elasticsearch green           1         1      0   0    0    0        0             0                  -                100.0%
```
7. You can find further instructions on how to configure and use Elasticsearch in the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).

onelinerhub: [How do I install Elasticsearch on Ubuntu?](https://onelinerhub.com/elasticsearch/how-do-i-install-elasticsearch-on-ubuntu)