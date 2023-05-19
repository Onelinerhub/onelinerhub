# How to rename a MongoDB collection?
// plain

MongoDB collections can be renamed using the `renameCollection()` method.

```
db.collection.renameCollection("newCollectionName")
```

This method takes two parameters:

1. The current collection name
2. The new collection name

The output of the above example code will be:
```
{ "ok" : 1 }
```

This indicates that the collection has been successfully renamed.

## Helpful links

- [MongoDB Documentation - renameCollection()](https://docs.mongodb.com/manual/reference/method/db.collection.renameCollection/)

onelinerhub: [How to rename a MongoDB collection?](https://onelinerhub.com/mongodb/how-to-rename-a-mongodb-collection)