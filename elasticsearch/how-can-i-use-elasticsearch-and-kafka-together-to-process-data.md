# How can I use Elasticsearch and Kafka together to process data?
// plain

Elasticsearch and Kafka can be used together to process data by consuming messages from Kafka topics and indexing them into Elasticsearch. For example, we can use the [Elasticsearch Kafka Connector](https://www.elastic.co/guide/en/elasticsearch/plugins/7.8/kafka-connector.html) to stream data from Kafka topics into Elasticsearch.

```
// Create the Kafka Connector
curl -X PUT "localhost:9200/_ingest/pipeline/kafka_connector_pipeline" -H 'Content-Type: application/json' -d'
{
  "description" : "Kafka Connector Pipeline",
  "processors" : [
    {
      "kafka" : {
        "topic" : "kafka_topic",
        "bootstrap.servers" : "localhost:9092",
        "group.id" : "kafka_group_id"
      }
    }
  ]
}
'
```

The output of the above command will be:
```
{
  "acknowledged": true
}
```

The code above creates a Kafka Connector Pipeline with the following parts:
- `curl`: a command-line tool for making HTTP requests.
- `-X PUT`: an option for `curl` that specifies the HTTP request method to use.
- `localhost:9200/_ingest/pipeline/kafka_connector_pipeline`: the URL of the Elasticsearch endpoint for creating a pipeline.
- `-H 'Content-Type: application/json'`: an option for `curl` that specifies the content type of the request body.
- `-d'`: an option for `curl` that specifies the data to be sent in the request body.
- `"kafka"`: the processor type for the Kafka Connector.
- `"topic" : "kafka_topic"`: the name of the Kafka topic to be consumed.
- `"bootstrap.servers" : "localhost:9092"`: the list of Kafka brokers to connect to.
- `"group.id" : "kafka_group_id"`: the ID of the Kafka consumer group.

By using the Kafka Connector, we can stream data from Kafka topics into Elasticsearch and process it in real-time.

## Helpful links
- [Elasticsearch Kafka Connector](https://www.elastic.co/guide/en/elasticsearch/plugins/7.8/kafka-connector.html)
- [Kafka Connector API](https://www.elastic.co/guide/en/elasticsearch/reference/current/connectors.html)

onelinerhub: [How can I use Elasticsearch and Kafka together to process data?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-and-kafka-together-to-process-data)