# How do I configure Elasticsearch with a YML file?
// plain

Configuration of Elasticsearch with a YML file can be done by editing the `elasticsearch.yml` file. This file is usually located in the `config` directory of the Elasticsearch installation. The file contains configuration settings for the Elasticsearch instance.

## Example code

```
# Configure the cluster name
cluster.name: my-cluster

# Configure node name
node.name: node-1
```

The first line of code configures the cluster name for the Elasticsearch instance. The second line configures the node name for the instance.

The configuration settings in the `elasticsearch.yml` file can be changed to customize the Elasticsearch instance. For example, the following can be configured:
- `http.port`: Configure the HTTP port used for communication.
- `node.data`: Enable or disable the node from storing data.
- `network.host`: Configure the network host to bind to.

Links:
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/configuring.html)
- [Elasticsearch Configuration File](https://www.elastic.co/guide/en/elasticsearch/reference/current/configuring-elasticsearch.html#config-file)

onelinerhub: [How do I configure Elasticsearch with a YML file?](https://onelinerhub.com/elasticsearch/how-do-i-configure-elasticsearch-with-a-yml-file)