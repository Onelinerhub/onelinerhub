# How to set MongoDB oplog?
// plain

MongoDB oplog is a special capped collection that keeps a rolling record of all operations that modify the data stored in your databases. To set up oplog, you need to start MongoDB with the `--replSet` option.

```
mongod --replSet myReplSet
```

Once the MongoDB instance is running, you can initiate the replica set using the `rs.initiate()` command.

```
rs.initiate()
```

## Code explanation


1. `mongod --replSet`: This command starts MongoDB with the `--replSet` option, which enables replication and sets up the oplog.

2. `rs.initiate()`: This command initiates the replica set and creates the oplog.

## Helpful links

- [MongoDB Replica Set Oplog](https://docs.mongodb.com/manual/core/replica-set-oplog/)
- [Replica Set Oplog Internals](https://docs.mongodb.com/manual/core/replica-set-oplog-internals/)

onelinerhub: [How to set MongoDB oplog?](https://onelinerhub.com/mongodb/how-to-set-mongodb-oplog)