# How can I use Docker Compose to set up Elasticsearch and Kibana?
// plain

Docker Compose can be used to quickly set up Elasticsearch and Kibana.

To get started, create a `docker-compose.yml` file and add the following configuration:

```
version: '2'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.8.0
    ports:
      - 9200:9200
    environment:
      - node.name=elasticsearch
      - discovery.type=single-node
  kibana:
    image: docker.elastic.co/kibana/kibana:7.8.0
    ports:
      - 5601:5601
    environment:
      - ELASTICSEARCH_URL=http://elasticsearch:9200
```

1. `version`: Specifies the version of the Docker Compose file format.
2. `services`: Defines the services to be run by Docker Compose.
3. `elasticsearch`: Defines the configuration for the Elasticsearch service.
4. `image`: Specifies the Docker image to be used for the Elasticsearch service.
5. `ports`: Specifies the port mapping for the Elasticsearch service.
6. `environment`: Specifies environment variables for the Elasticsearch service.
7. `kibana`: Defines the configuration for the Kibana service.
8. `image`: Specifies the Docker image to be used for the Kibana service.
9. `ports`: Specifies the port mapping for the Kibana service.
10. `environment`: Specifies environment variables for the Kibana service.

Once the configuration is in place, run the following command to start the services:

```
docker-compose up -d
```

The output should look like this:

```
Creating network "docker_default" with the default driver
Creating docker_elasticsearch_1 ... done
Creating docker_kibana_1      ... done
```

The two services should now be up and running. You can verify this by running `docker-compose ps`:

```
Name               Command              State           Ports
----------------------------------------------------------------
docker_elasticsearch_1   /usr/local/bin/docker-entr ...   Up      0.0.0.0:9200->9200/tcp, 9300/tcp
docker_kibana_1      /usr/local/bin/dumb-init - ...   Up      0.0.0.0:5601->5601/tcp
```

You can now access the Elasticsearch and Kibana services on the specified ports.

## Helpful links
- https://docs.docker.com/compose/
- https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
- https://www.elastic.co/guide/en/kibana/current/docker.html

onelinerhub: [How can I use Docker Compose to set up Elasticsearch and Kibana?](https://onelinerhub.com/elasticsearch/how-can-i-use-docker-compose-to-set-up-elasticsearch-and-kibana)