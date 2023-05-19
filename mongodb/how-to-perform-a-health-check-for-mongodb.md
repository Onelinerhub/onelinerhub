# How to perform a health check for MongoDB?
// plain

A health check for MongoDB can be performed using the `db.serverStatus()` command. This command will return a document containing a variety of metrics about the current state of the server.

```
> db.serverStatus()
{
  "host" : "localhost:27017",
  "version" : "4.2.3",
  "process" : "mongod",
  "pid" : NumberLong(12345),
  "uptime" : NumberLong(12345),
  "uptimeMillis" : NumberLong(12345),
  "uptimeEstimate" : NumberLong(12345),
  "localTime" : ISODate("2020-01-01T00:00:00.000Z"),
  "asserts" : {
    "regular" : 0,
    "warning" : 0,
    "msg" : 0,
    "user" : 0,
    "rollovers" : 0
  },
  "connections" : {
    "current" : 5,
    "available" : 2095,
    "totalCreated" : NumberLong(12345)
  },
  "extra_info" : {
    "note" : "fields vary by platform",
    "heap_usage_bytes" : NumberLong(12345),
    "page_faults" : NumberLong(12345)
  },
  "ok" : 1
}
```

The output of the command will provide information about the server's host, version, process, uptime, local time, asserts, connections, and extra info. This information can be used to assess the health of the MongoDB server.

## Code explanation


- `db.serverStatus()`: command to perform a health check for MongoDB
- `host`: hostname of the MongoDB server
- `version`: version of the MongoDB server
- `process`: process name of the MongoDB server
- `pid`: process ID of the MongoDB server
- `uptime`: uptime of the MongoDB server in seconds
- `uptimeMillis`: uptime of the MongoDB server in milliseconds
- `uptimeEstimate`: estimated uptime of the MongoDB server
- `localTime`: local time of the MongoDB server
- `asserts`: number of assertions made by the MongoDB server
- `connections`: number of current, available, and total connections to the MongoDB server
- `extra_info`: additional information about the MongoDB server
- `ok`: status of the MongoDB server (1 for success, 0 for failure)

## Helpful links

- [MongoDB Documentation - db.serverStatus()](https://docs.mongodb.com/manual/reference/command/serverStatus/)

onelinerhub: [How to perform a health check for MongoDB?](https://onelinerhub.com/mongodb/how-to-perform-a-health-check-for-mongodb)