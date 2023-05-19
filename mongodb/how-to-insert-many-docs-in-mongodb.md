# How to insert many docs in MongoDB?
// plain

MongoDB provides a bulk insert operation to insert multiple documents into a collection. The syntax for bulk insert is as follows:

```
db.collection.insertMany(
   [
      { <document 1> },
      { <document 2> },
      ...
      { <document n> }
   ]
)
```

The output of the above command will be:

```
{
   "acknowledged" : true,
   "insertedIds" : [
      ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f"),
      ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f"),
      ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f")
   ]
}
```

## Code explanation


- `db.collection.insertMany`: This is the method used to perform a bulk insert operation.
- `[ { <document 1> }, { <document 2> }, ... { <document n> } ]`: This is an array of documents to be inserted.
- `acknowledged`: This is a boolean value indicating whether the operation was successful or not.
- `insertedIds`: This is an array of ObjectIds of the documents that were inserted.

## Helpful links

- [MongoDB Documentation - Bulk Write Operations](https://docs.mongodb.com/manual/reference/method/db.collection.insertMany/)

onelinerhub: [How to insert many docs in MongoDB?](https://onelinerhub.com/mongodb/how-to-insert-many-docs-in-mongodb)