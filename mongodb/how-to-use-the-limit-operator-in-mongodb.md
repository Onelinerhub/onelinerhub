# How to use the limit operator in MongoDB?
// plain

The `limit()` operator in MongoDB is used to limit the number of documents returned in a query. It is used in conjunction with the `find()` method.

## Example

```
db.collection.find().limit(5)
```

This will return the first 5 documents from the collection.

## Code explanation

- `db.collection.find()`: This is the method used to query the collection.
- `.limit(5)`: This is the limit operator, which limits the number of documents returned to 5.

## Helpful links
- [MongoDB Limit Operator](https://docs.mongodb.com/manual/reference/operator/query/limit/)

onelinerhub: [How to use the limit operator in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-the-limit-operator-in-mongodb)