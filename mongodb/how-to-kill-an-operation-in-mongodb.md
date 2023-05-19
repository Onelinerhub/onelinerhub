# How to kill an operation in MongoDB?
// plain

To kill an operation in MongoDB, you can use the `db.killOp()` method. This method takes a single parameter, the operation ID, which can be obtained from the `db.currentOp()` method.

## Example

```
> db.currentOp()
{
  "inprog" : [
    {
      "opid" : NumberLong(123456789),
      "active" : true,
      "secs_running" : NumberLong(123),
      "op" : "query",
      "ns" : "mydb.mycollection",
      "query" : {
        "find" : "mycollection"
      },
      "client" : "127.0.0.1:12345",
      "desc" : "conn12345",
      "threadId" : "123456789",
      "connectionId" : 12345,
      "locks" : {
        "^" : "W"
      },
      "waitingForLock" : false,
      "numYields" : 0,
      "lockStats" : {
        "timeLockedMicros" : {
          "r" : NumberLong(12345),
          "w" : NumberLong(12345)
        },
        "timeAcquiringMicros" : {
          "r" : NumberLong(12345),
          "w" : NumberLong(12345)
        }
      }
    }
  ]
}
```

To kill the operation with the ID `123456789`, you can use the following command:

```
> db.killOp(123456789)
{ "info" : "attempting to kill op", "ok" : 1 }
```

The `db.killOp()` method takes a single parameter, the operation ID, which can be obtained from the `db.currentOp()` method. The `db.currentOp()` method returns a list of operations currently running on the server, including the operation ID, the type of operation, the namespace, the query, and other information. The `db.killOp()` method then takes the operation ID and attempts to kill the operation.

## Helpful links
- [MongoDB Documentation - db.killOp()](https://docs.mongodb.com/manual/reference/method/db.killOp/)
- [MongoDB Documentation - db.currentOp()](https://docs.mongodb.com/manual/reference/method/db.currentOp/)

onelinerhub: [How to kill an operation in MongoDB?](https://onelinerhub.com/mongodb/how-to-kill-an-operation-in-mongodb)