# How to install MongoDB with Docker?
// plain

1. Install Docker on your machine. Refer to the [Docker installation guide](https://docs.docker.com/install/) for instructions.

2. Pull the MongoDB image from the Docker Hub.

```
docker pull mongo
```

3. Run the MongoDB container.

```
docker run --name my-mongo -d mongo
```

4. Check the container is running.

```
docker ps
```

## Output example

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
f8f9f9f9f9f9        mongo               "docker-entrypoint.s…"   5 minutes ago       Up 5 minutes        27017/tcp           my-mongo
```

5. Connect to the MongoDB instance.

```
docker exec -it my-mongo mongo
```

group: docker

onelinerhub: [How to install MongoDB with Docker?](https://onelinerhub.com/mongodb/how-to-install-mongodb-with-docker)