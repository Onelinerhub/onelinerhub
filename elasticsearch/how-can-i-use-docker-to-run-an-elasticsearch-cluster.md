# How can I use Docker to run an Elasticsearch cluster?
// plain

Using Docker to run an Elasticsearch cluster is a great way to quickly spin up a cluster of Elasticsearch nodes for development and testing.

To get started, you'll need to install Docker on your machine. Once you have Docker installed, you can create a Docker container for each node in your Elasticsearch cluster. Here's an example of how to create a Docker container for an Elasticsearch node:

```
docker run -d --name elasticsearch-node-1 -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.7.0
```

This command will create a Docker container named "elasticsearch-node-1" and it will use port 9200 for communication. It also sets the "discovery.type" parameter to "single-node" so that the node will join a single-node cluster.

Once you have created all the nodes in your cluster, you can use the Elasticsearch API to add and remove nodes from the cluster. For example, to add a node to the cluster, you can use the following API call:

```
POST http://localhost:9200/_cluster/nodes
```

This API call will add a node to the cluster with the same settings as the other nodes.

Finally, you can use the Elasticsearch API to verify that the cluster is running correctly. You can do this by making a GET request to the cluster health endpoint:

```
GET http://localhost:9200/_cluster/health
```

The response will include information about the status of the cluster, such as the number of nodes, the status of the primary shard, and the cluster state.

## Helpful links
- [Docker Documentation](https://docs.docker.com/)
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

onelinerhub: [How can I use Docker to run an Elasticsearch cluster?](https://onelinerhub.com/elasticsearch/how-can-i-use-docker-to-run-an-elasticsearch-cluster)