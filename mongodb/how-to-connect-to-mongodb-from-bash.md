# How to connect to MongoDB from bash?
// plain

You can connect to MongoDB from bash using the `mongo` command.

```
$ mongo
MongoDB shell version v4.2.3
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("f9f9f9f9-f9f9-f9f9-f9f9-f9f9f9f9f9f9") }
MongoDB server version: 4.2.3
```

The `mongo` command takes the following parameters:

- `--host`: The hostname of the MongoDB instance.
- `--port`: The port of the MongoDB instance.
- `--username`: The username to authenticate with.
- `--password`: The password to authenticate with.
- `--authenticationDatabase`: The authentication database to use.

For more information, see the [MongoDB documentation](https://docs.mongodb.com/manual/reference/program/mongo/).

onelinerhub: [How to connect to MongoDB from bash?](https://onelinerhub.com/mongodb/how-to-connect-to-mongodb-from-bash)