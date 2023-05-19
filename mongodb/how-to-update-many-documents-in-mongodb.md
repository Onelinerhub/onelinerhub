# How to update many documents in MongoDB?
// plain

Updating many documents in MongoDB can be done using the `updateMany()` method. This method takes two parameters: a filter object and an update object. The filter object is used to specify which documents should be updated, and the update object is used to specify the changes to be made.

## Example

```
db.collection.updateMany(
  { "name": "John" },
  { $set: { "age": 30 } }
)
```

## Output example

```
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

## Code explanation

- `updateMany()`: The method used to update many documents in MongoDB.
- `{ "name": "John" }`: The filter object used to specify which documents should be updated.
- `{ $set: { "age": 30 } }`: The update object used to specify the changes to be made.

## Helpful links
- [MongoDB Documentation - updateMany()](https://docs.mongodb.com/manual/reference/method/db.collection.updateMany/)

onelinerhub: [How to update many documents in MongoDB?](https://onelinerhub.com/mongodb/how-to-update-many-documents-in-mongodb)