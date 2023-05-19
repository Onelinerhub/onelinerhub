# How to update one document in MongoDB?
// plain

Updating a document in MongoDB is a simple process. The following example code block shows how to update a document in MongoDB using the `updateOne()` method:

```
db.collection.updateOne(
   <filter>,
   <update>,
   {
     upsert: <boolean>,
     writeConcern: <document>
   }
)
```

The `updateOne()` method takes three parameters:

1. `filter`: A document that specifies the criteria for selecting the document to update.
2. `update`: A document that specifies the modifications to apply to the document.
3. `options`: An optional parameter that specifies additional options for the update operation.

The output of the example code above would be a `UpdateResult` object, which contains information about the update operation.

For more information, please refer to the [MongoDB documentation](https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/).

onelinerhub: [How to update one document in MongoDB?](https://onelinerhub.com/mongodb/how-to-update-one-document-in-mongodb)