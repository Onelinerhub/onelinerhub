# How to bulk update documents in MongoDB?
// plain

MongoDB provides a bulk update operation to update multiple documents in a single operation. The syntax for bulk update is as follows:

```
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
```

- `<query>`: Specifies the selection criteria for the update.
- `<update>`: Specifies the modifications to be made to the documents that match the query.
- `upsert`: Optional. If set to true, creates a new document when no document matches the query criteria.
- `multi`: Optional. If set to true, updates multiple documents that meet the query criteria. If set to false, updates one document.
- `writeConcern`: Optional. A document expressing the write concern.

For example, the following operation updates all documents in the collection that have a `qty` field equal to 0 with an `updatedQty` field equal to 20:

```
db.collection.update(
   { qty: 0 },
   { $set: { updatedQty: 20 } },
   { multi: true }
)
```

## Helpful links
- [MongoDB Documentation - Bulk Write Operations](https://docs.mongodb.com/manual/reference/method/db.collection.bulkWrite/)

onelinerhub: [How to bulk update documents in MongoDB?](https://onelinerhub.com/mongodb/how-to-bulk-update-documents-in-mongodb)