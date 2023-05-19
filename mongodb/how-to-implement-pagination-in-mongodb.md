# How to implement pagination in MongoDB?
// plain

Pagination in MongoDB can be implemented using the `skip()` and `limit()` methods. The `skip()` method skips a specified number of documents from the beginning of the result set, and the `limit()` method limits the number of documents returned.

For example, the following code will return the second page of 10 documents from the collection `users`:

```
db.users.find().skip(10).limit(10)
```

The code above will return the following output:

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "John Doe", "age" : 25 }
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "Jane Doe", "age" : 30 }
...
```

The code consists of the following parts:

- `db.users.find()`: This is the query that will return all documents from the `users` collection.
- `skip(10)`: This will skip the first 10 documents from the result set.
- `limit(10)`: This will limit the number of documents returned to 10.

For more information, see the [MongoDB documentation](https://docs.mongodb.com/manual/reference/method/js-cursor/).

onelinerhub: [How to implement pagination in MongoDB?](https://onelinerhub.com/mongodb/how-to-implement-pagination-in-mongodb)