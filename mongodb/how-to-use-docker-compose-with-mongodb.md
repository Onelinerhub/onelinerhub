# How to use Docker Compose with MongoDB?
// plain

Docker Compose is a tool for defining and running multi-container Docker applications. It can be used to easily set up and run a MongoDB instance in a Docker container.

To use Docker Compose with MongoDB, create a `docker-compose.yml` file with the following content:

```
version: '3'
services:
  mongodb:
    image: mongo
    ports:
      - 27017:27017
```

Then, run `docker-compose up` to start the MongoDB instance.

The code above:

- `version: '3'`: specifies the version of the Docker Compose file format
- `services`: defines the services that will be run in the Docker Compose application
- `mongodb`: the name of the service
- `image`: the Docker image to use for the service
- `ports`: the ports to expose from the container

For more information, see the [Docker Compose documentation](https://docs.docker.com/compose/).

group: docker

onelinerhub: [How to use Docker Compose with MongoDB?](https://onelinerhub.com/mongodb/how-to-use-docker-compose-with-mongodb)