# How can I use Elasticsearch and Logstash together to collect and analyze log data?
// plain

Elasticsearch and Logstash can be used together to collect and analyze log data.

Logstash can be used to collect the log data from a variety of sources. It can then parse, filter, and transform the log data before sending it to Elasticsearch for storage and analysis.

For example, the following Logstash configuration can be used to collect log data from a file and send it to Elasticsearch:
```
input {
  file {
    path => "/var/log/myapp/app.log"
  }
}

filter {
  # Parse the log file
  grok {
    match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:loglevel} %{GREEDYDATA:message}" }
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
  }
}
```

This configuration will read the log file `/var/log/myapp/app.log`, parse it using the Grok filter, and send the parsed data to Elasticsearch.

Once the data is in Elasticsearch, it can be queried and analyzed using the Elasticsearch Query DSL. For example, the following query can be used to find all log messages with the log level ERROR:

```
GET /_search
{
  "query": {
    "match": {
      "loglevel": "ERROR"
    }
  }
}
```

The output of this query will be a list of documents from Elasticsearch that match the query criteria.

By using Logstash and Elasticsearch together, it is possible to collect and analyze log data quickly and easily.

## Helpful links
* [Logstash Documentation](https://www.elastic.co/guide/en/logstash/current/index.html)
* [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
* [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [How can I use Elasticsearch and Logstash together to collect and analyze log data?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-and-logstash-together-to-collect-and-analyze-log-data)