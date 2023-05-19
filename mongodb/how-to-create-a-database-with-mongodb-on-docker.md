# How to create a database with MongoDB on Docker?
// plain

Creating a MongoDB database with Docker is a simple process.

1. Pull the MongoDB image from Docker Hub:
```
docker pull mongo
```
2. Run the MongoDB container:
```
docker run -d -p 27017:27017 --name mongodb mongo
```
3. Connect to the MongoDB container:
```
docker exec -it mongodb bash
```
4. Create a database:
```
mongo
use my_database
```

The above steps will create a MongoDB database called `my_database` on Docker.

## Helpful links
- [MongoDB Docker Hub](https://hub.docker.com/_/mongo)
- [MongoDB Documentation](https://docs.mongodb.com/manual/)

group: docker

onelinerhub: [How to create a database with MongoDB on Docker?](https://onelinerhub.com/mongodb/how-to-create-a-database-with-mongodb-on-docker)