# How can I use Docker to deploy Elasticsearch and Kibana?
// plain

To deploy Elasticsearch and Kibana using Docker, you can use the official images from the Docker Hub.

1. Pull the images from the Docker Hub:
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.9.2
docker pull docker.elastic.co/kibana/kibana:7.9.2
```

2. Create a network for the containers:
```
docker network create elastic
```

3. Start the Elasticsearch container:
```
docker run -d --name elasticsearch --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.9.2
```

4. Start the Kibana container:
```
docker run -d --name kibana --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:7.9.2
```

You can now access Elasticsearch and Kibana on the host machine.

## Helpful links
- [Docker Hub - Elasticsearch](https://hub.docker.com/_/elasticsearch)
- [Docker Hub - Kibana](https://hub.docker.com/_/kibana)

onelinerhub: [How can I use Docker to deploy Elasticsearch and Kibana?](https://onelinerhub.com/elasticsearch/how-can-i-use-docker-to-deploy-elasticsearch-and-kibana)