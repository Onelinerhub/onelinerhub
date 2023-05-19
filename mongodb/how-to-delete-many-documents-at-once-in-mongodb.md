# How to delete many documents at once in MongoDB?
// plain

MongoDB provides a `deleteMany()` method to delete multiple documents from a collection. The syntax for `deleteMany()` is as follows:

```
db.collection.deleteMany(
   <filter>,
   {
     justOne: <boolean>,
     writeConcern: <document>
   }
)
```

- `<filter>`: Specifies the selection criteria to delete the documents.
- `justOne`: Optional. To delete only one document, set to `true`. The default value is `false`, which deletes all documents that match the criteria.
- `writeConcern`: Optional. A document expressing the write concern.

For example, the following operation deletes all documents in the collection `inventory` where the `status` field equals `A`:

```
db.inventory.deleteMany( { status : "A" } )
```

The output of the above example will be:

```
{ "acknowledged" : true, "deletedCount" : 3 }
```

For more information, please refer to the [MongoDB documentation](https://docs.mongodb.com/manual/reference/method/db.collection.deleteMany/).

onelinerhub: [How to delete many documents at once in MongoDB?](https://onelinerhub.com/mongodb/how-to-delete-many-documents-at-once-in-mongodb)