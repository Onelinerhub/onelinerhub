# image

How do I use the official Sphinxsearch Docker image?
// plain

The official Sphinxsearch Docker image can be used to quickly deploy a Sphinxsearch instance in a container. To use the image, first pull it from the Docker Hub using the following command:

```
docker pull sphinxsearch/sphinxsearch
```

Then, start the container with the following command:

```
docker run -d --name sphinxsearch -p 9306:9306 sphinxsearch/sphinxsearch
```

This will start the Sphinxsearch instance in the background, and will forward port 9306 from the container to the host. To access the instance, the following command can be used:

```
docker exec -it sphinxsearch /bin/bash
```

This will launch a Bash session within the container, allowing you to access the Sphinxsearch instance. Finally, you can start the searchd service by running the following command:

```
searchd --config /etc/sphinxsearch/sphinx.conf
```

The Sphinxsearch instance will now be running and accessible from the host.

## Code explanation


1. `docker pull sphinxsearch/sphinxsearch` - Pulls the Sphinxsearch image from the Docker Hub
2. `docker run -d --name sphinxsearch -p 9306:9306 sphinxsearch/sphinxsearch` - Starts the container in the background, forwarding port 9306
3. `docker exec -it sphinxsearch /bin/bash` - Launches a Bash session within the container
4. `searchd --config /etc/sphinxsearch/sphinx.conf` - Starts the searchd service

## Helpful links

- [Sphinxsearch Docker Hub Page](https://hub.docker.com/r/sphinxsearch/sphinxsearch)

onelinerhub: [image

How do I use the official Sphinxsearch Docker image?](https://onelinerhub.com/sphinxsearch/image--how-do-i-use-the-official-sphinxsearch-docker-image)