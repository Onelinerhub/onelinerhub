# How can I use Docker Compose to configure and deploy an Elasticsearch cluster?
// plain

**Docker Compose** can be used to configure and deploy an **Elasticsearch cluster**. Here's an example of how to do this:

```
version: '3.2'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.7.0
    environment:
      - cluster.name=docker-cluster
      - discovery.type=single-node
    ports:
      - 9200:9200
```

This example creates a `docker-cluster` cluster with a single node. This is done by setting the environment variable `cluster.name` to `docker-cluster` and the environment variable `discovery.type` to `single-node`. The `image` directive is used to specify the version of Elasticsearch to be used (in this case, 7.7.0). Finally, the `ports` directive is used to map the host's port 9200 to the container's port 9200.

Once the configuration is in place, the cluster can be deployed using the `docker-compose` command:

```
$ docker-compose up
```

This command will start the Elasticsearch cluster.

Parts of the example code:

* `version`: specifies the version of the Docker Compose file format
* `services`: defines the services to be deployed
* `image`: specifies the version of Elasticsearch to be used
* `environment`: defines the environment variables to set
* `ports`: maps host ports to container ports

## Helpful links

* [Docker Compose Documentation](https://docs.docker.com/compose/)
* [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

onelinerhub: [How can I use Docker Compose to configure and deploy an Elasticsearch cluster?](https://onelinerhub.com/elasticsearch/how-can-i-use-docker-compose-to-configure-and-deploy-an-elasticsearch-cluster)