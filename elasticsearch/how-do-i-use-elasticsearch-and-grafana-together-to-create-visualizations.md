# How do I use Elasticsearch and Grafana together to create visualizations?
// plain

Grafana and Elasticsearch can be used together to create visualizations. To do this, first install and configure Grafana and Elasticsearch. Then, create a data source in Grafana that connects to the Elasticsearch instance. After the data source is set up, create a new dashboard and add a graph visualization. Finally, configure the graph visualization to show the desired data from the Elasticsearch instance.

## Example code

```
# Create data source
$ curl -X POST \
  http://localhost:3000/api/datasources \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Elasticsearch",
    "type": "elasticsearch",
    "url": "http://localhost:9200",
    "access": "proxy"
}'

# Create graph visualization
$ curl -X POST \
  http://localhost:3000/api/dashboards/db \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "My Dashboard",
    "panels": [
        {
            "type": "graph",
            "datasource": "Elasticsearch",
            "title": "My Graph Visualization"
        }
    ]
}'
```

Then, configure the graph visualization to show the desired data from the Elasticsearch instance. This can be done by using the query editor to create the query that will be used to retrieve the data from the Elasticsearch instance.

## Code explanation

- `curl -X POST`: Sends an HTTP POST request to the specified URL.
- `http://localhost:3000/api/datasources`: The URL of the Grafana API endpoint for creating data sources.
- `http://localhost:9200`: The URL of the Elasticsearch instance.
- `"type": "elasticsearch"`: Specifies that the data source is an Elasticsearch instance.
- `http://localhost:3000/api/dashboards/db`: The URL of the Grafana API endpoint for creating dashboards.
- `"type": "graph"`: Specifies that the visualization is a graph.
- `"datasource": "Elasticsearch"`: Specifies that the data source is the Elasticsearch instance.

## Helpful links
- [Grafana Documentation](https://grafana.com/docs/grafana/latest/)
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

onelinerhub: [How do I use Elasticsearch and Grafana together to create visualizations?](https://onelinerhub.com/elasticsearch/how-do-i-use-elasticsearch-and-grafana-together-to-create-visualizations)