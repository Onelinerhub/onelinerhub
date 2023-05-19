# How to specify a password for MongoDB Docker?
// plain

MongoDB Docker can be configured to use a password for authentication. To do this, you need to set the `MONGO_INITDB_ROOT_USERNAME` and `MONGO_INITDB_ROOT_PASSWORD` environment variables when running the container.

## Example

```
docker run -d -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password \
  mongo
```

This will create a MongoDB container with the username `admin` and password `password`.

## Code explanation

- `docker run`: Runs a command in a new container
- `-d`: Runs the container in detached mode, meaning it runs in the background
- `-p 27017:27017`: Maps the container's port 27017 to the host's port 27017
- `-e MONGO_INITDB_ROOT_USERNAME=admin`: Sets the environment variable `MONGO_INITDB_ROOT_USERNAME` to `admin`
- `-e MONGO_INITDB_ROOT_PASSWORD=password`: Sets the environment variable `MONGO_INITDB_ROOT_PASSWORD` to `password`
- `mongo`: The image to use for the container

## Helpful links
- [MongoDB Docker Documentation](https://docs.mongodb.com/manual/tutorial/deploy-mongodb-on-docker/)

group: docker

onelinerhub: [How to specify a password for MongoDB Docker?](https://onelinerhub.com/mongodb/how-to-specify-a-password-for-mongodb-docker)