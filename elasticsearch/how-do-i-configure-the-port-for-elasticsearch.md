# How do I configure the port for Elasticsearch?
// plain

To configure the port for Elasticsearch, you need to modify the `elasticsearch.yml` file. This file is located in the `config` directory within the Elasticsearch home directory.

The `elasticsearch.yml` file contains settings for the Elasticsearch node. To configure the port, you will need to add the following line to the file:

```
http.port: 9200
```

This will configure the port to `9200`. You can replace `9200` with any port number you want. Once you have made the change, you will need to restart the Elasticsearch node for the changes to take effect.

You can also configure the port using the `-E` flag when starting Elasticsearch. For example:

```
bin/elasticsearch -Ehttp.port=9200
```

The above command will start the Elasticsearch node on port `9200`.

## Code explanation


- `elasticsearch.yml`: This is the configuration file for the Elasticsearch node. It contains settings for the node and is located in the `config` directory within the Elasticsearch home directory.
- `http.port`: This setting is used to configure the port for the Elasticsearch node.
- `-E` flag: This flag is used when starting Elasticsearch to configure settings.

## Helpful links

- [Elasticsearch Configuration](https://www.elastic.co/guide/en/elasticsearch/reference/current/settings.html)
- [Elasticsearch Command Line Options](https://www.elastic.co/guide/en/elasticsearch/reference/current/command-line-options.html)

onelinerhub: [How do I configure the port for Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-configure-the-port-for-elasticsearch)