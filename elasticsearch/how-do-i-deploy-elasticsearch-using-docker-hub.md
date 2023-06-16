# How do I deploy Elasticsearch using Docker Hub?
// plain

1. Deploying Elasticsearch using Docker Hub is quite simple.
2. First, pull the Elasticsearch image from Docker Hub with the following command:
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.9.2
```
3. Then, run the image with the following command:
```
docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.9.2
```
4. This will start the Elasticsearch instance, and you should see the following output:
```
d5c8e8e9c2d4: Elasticsearch 7.9.2
```
5. You can then access the Elasticsearch instance from your browser, using the URL http://localhost:9200.
6. You can also use the following command to check the status of the Elasticsearch instance:
```
docker ps
```
7. This will output the running container, and you can check the status of the Elasticsearch instance.

## Helpful links
- [Docker Hub](https://hub.docker.com)
- [Elasticsearch Docker Image](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

onelinerhub: [How do I deploy Elasticsearch using Docker Hub?](https://onelinerhub.com/elasticsearch/how-do-i-deploy-elasticsearch-using-docker-hub)