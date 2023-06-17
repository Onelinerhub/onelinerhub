# How can I configure an Elasticsearch Prometheus exporter?
// plain

The Elasticsearch Prometheus exporter is a tool used to monitor the performance of an Elasticsearch cluster. It can be configured by following these steps:

1. Download the Prometheus exporter from [GitHub](https://github.com/vvanholl/elasticsearch_exporter).

2. Extract the files and run the binary `elasticsearch_exporter` with the appropriate flags. For example:

```
./elasticsearch_exporter --es.uri http://localhost:9200
```

3. This will start the exporter and listen on port 9114.

4. Create a Prometheus configuration file (e.g. `prometheus.yml`) and add the exporter as a target. For example:

```
scrape_configs:
  - job_name: 'elasticsearch_exporter'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9114']
```

5. Start Prometheus with the configuration file. For example:

```
prometheus --config.file=prometheus.yml
```

6. The exporter will now be scraped by Prometheus and the metrics will be available in the Prometheus UI.

7. Additionally, the metrics can be used to create alerts and dashboards in Grafana.

onelinerhub: [How can I configure an Elasticsearch Prometheus exporter?](https://onelinerhub.com/elasticsearch/how-can-i-configure-an-elasticsearch-prometheus-exporter)