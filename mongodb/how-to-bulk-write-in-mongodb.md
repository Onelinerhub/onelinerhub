# How to bulk write in MongoDB?
// plain

MongoDB provides a bulk write operation that allows users to perform multiple write operations in one request. This operation can be used to insert, update, and delete multiple documents in a single request.

## Example code

```
db.collection.bulkWrite([
  { insertOne: { document: { a: 1 } } },
  { updateOne: { filter: { a: 2 }, update: { $set: { a: 2 } }, upsert: true } },
  { deleteOne: { filter: { a: 3 } } }
])
```

## Output example

```
{
  "acknowledged" : true,
  "deletedCount" : 1,
  "insertedCount" : 1,
  "matchedCount" : 1,
  "upsertedCount" : 1,
  "insertedIds" : [
    ObjectId("5f3f9f9f8f9f9f9f9f9f9f9f")
  ],
  "upsertedIds" : [
    ObjectId("5f3f9f9f8f9f9f9f9f9f9f9f")
  ]
}
```

## Code explanation

- `db.collection.bulkWrite()`: This is the method used to perform the bulk write operation.
- `insertOne`: This is the operation used to insert a single document.
- `updateOne`: This is the operation used to update a single document.
- `deleteOne`: This is the operation used to delete a single document.
- `filter`: This is the filter used to specify which documents should be affected by the operation.
- `update`: This is the update document used to specify the changes to be made to the documents.
- `upsert`: This is a boolean flag used to specify whether a new document should be inserted if no documents match the filter.

## Helpful links
- [MongoDB Bulk Write Documentation](https://docs.mongodb.com/manual/reference/method/db.collection.bulkWrite/)

onelinerhub: [How to bulk write in MongoDB?](https://onelinerhub.com/mongodb/how-to-bulk-write-in-mongodb)