# What is MongoDB default port?
// plain

MongoDB default port is `27017`. It is the port on which MongoDB server listens for client connections.

Example code to connect to MongoDB server on default port:
```
mongo --host 127.0.0.1 --port 27017
```

Output of the above code:
```
MongoDB shell version v4.2.3
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("f9f9f9f9-f9f9-f9f9-f9f9-f9f9f9f9f9f9") }
MongoDB server version: 4.2.3
```

The code above connects to MongoDB server running on `127.0.0.1` (localhost) on port `27017`.

## Helpful links

- [MongoDB Documentation - Default Port](https://docs.mongodb.com/manual/reference/default-mongodb-port/)
- [MongoDB Documentation - Connect to MongoDB](https://docs.mongodb.com/manual/tutorial/connect-to-mongodb/)

onelinerhub: [What is MongoDB default port?](https://onelinerhub.com/mongodb/what-is-mongodb-default-port)