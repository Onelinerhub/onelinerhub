# How to set up a MongoDB replica with Docker Compose?
// plain

Setting up a MongoDB replica with Docker Compose is a straightforward process.

1. Create a `docker-compose.yml` file with the following content:

```
version: '3'
services:
  mongo-primary:
    image: mongo
    ports:
      - 27017:27017
    volumes:
      - ./data/primary:/data/db
    command: mongod --replSet rs0
  mongo-secondary:
    image: mongo
    ports:
      - 27018:27017
    volumes:
      - ./data/secondary:/data/db
    command: mongod --replSet rs0
```

2. Start the containers with `docker-compose up -d`

3. Connect to the primary container with `docker exec -it mongo-primary mongo`

4. Initialize the replica set with the following command:

```
rs.initiate(
  {
    _id: "rs0",
    members: [
      { _id: 0, host: "mongo-primary:27017" },
      { _id: 1, host: "mongo-secondary:27017" }
    ]
  }
)
```

5. Verify the replica set is working with `rs.status()`

## Helpful links
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [MongoDB Replica Set Documentation](https://docs.mongodb.com/manual/replication/)

group: docker

onelinerhub: [How to set up a MongoDB replica with Docker Compose?](https://onelinerhub.com/mongodb/how-to-set-up-a-mongodb-replica-with-docker-compose)