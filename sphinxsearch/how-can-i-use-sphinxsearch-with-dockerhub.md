# How can I use SphinxSearch with DockerHub?
// plain

SphinxSearch can be used with DockerHub by creating a Docker image that includes the SphinxSearch software. To do this, you can use the following example code to create a Dockerfile:

```
FROM ubuntu

RUN apt-get update && apt-get install -y sphinxsearch

CMD ["searchd", "--nodetach"]
```

This example code will create a Docker image based on Ubuntu and install SphinxSearch. The `CMD` command is used to start the searchd daemon when the container is launched.

Once the Dockerfile is created, you can build the Docker image with the following command:

```
docker build -t sphinxsearch .
```

This will create an image named `sphinxsearch` based on the Dockerfile. You can then push the image to DockerHub using the following command:

```
docker push sphinxsearch
```

Once the image is pushed to DockerHub, it can be used by other users.

Parts of the code:

- `FROM ubuntu`: This line specifies the base image that the Dockerfile will use. In this case, it is Ubuntu.

- `RUN apt-get update && apt-get install -y sphinxsearch`: This command will update the apt package list and install SphinxSearch.

- `CMD ["searchd", "--nodetach"]`: This command will start the searchd daemon when the container is launched.

## Helpful links

- [Docker Documentation](https://docs.docker.com/engine/reference/builder/)
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How can I use SphinxSearch with DockerHub?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-with-dockerhub)