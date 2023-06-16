# How can I use Elasticsearch, Kibana, and Logstash together for log analysis?
// plain

Elasticsearch, Kibana, and Logstash can be used together to analyze logs. Logstash is used to ingest and parse logs, Kibana is used to visualize the logs, and Elasticsearch is used to store the logs.

## Example code

```
input {
  file {
    path => "/var/log/syslog"
  }
}

filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
}

output {
  elasticsearch { hosts => ["localhost:9200"] }
  stdout { codec => rubydebug }
}
```

Output of example code:
```
{
  "message" => "127.0.0.1 - - [28/Jul/2006:10:27:10 -0300] \"GET / HTTP/1.1\" 200 44",
  "@version" => "1",
  "@timestamp" => 2018-09-20T19:38:52.902Z,
  "host" => "127.0.0.1",
  "clientip" => "127.0.0.1",
  "ident" => "-",
  "auth" => "-",
  "timestamp" => "28/Jul/2006:10:27:10 -0300",
  "verb" => "GET",
  "request" => "/",
  "httpversion" => "1.1",
  "response" => "200",
  "bytes" => "44"
}
```

## Code explanation

- input: This is the section of the configuration file that specifies the source of the log data. In this example, the log data is being read from the file located at `/var/log/syslog`.
- filter: This is the section of the configuration file that specifies the parsing of the log data. In this example, the log data is being parsed using the Grok filter.
- output: This is the section of the configuration file that specifies the destination of the parsed log data. In this example, the parsed log data is being sent to Elasticsearch and printed to the console.

List of ## Helpful links
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/index.html)
- [Logstash Documentation](https://www.elastic.co/guide/en/logstash/current/index.html)

onelinerhub: [How can I use Elasticsearch, Kibana, and Logstash together for log analysis?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch--kibana--and-logstash-together-for-log-analysis)