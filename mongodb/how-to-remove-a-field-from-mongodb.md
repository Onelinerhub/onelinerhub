# How to remove a field from MongoDB?
// plain

To remove a field from MongoDB, use the `$unset` operator. This operator removes the specified field from the document.

## Example

```
db.collection.update(
   { _id: 1 },
   { $unset: { field: "" } }
)
```

The output of the above example will be:
```
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

## Code explanation

- `db.collection.update`: This is the command used to update a document in MongoDB.
- `{ _id: 1 }`: This is the filter used to specify the document to update.
- `{ $unset: { field: "" } }`: This is the update operator used to remove the specified field from the document.

## Helpful links
- [MongoDB Documentation - $unset](https://docs.mongodb.com/manual/reference/operator/update/unset/)

onelinerhub: [How to remove a field from MongoDB?](https://onelinerhub.com/mongodb/how-to-remove-a-field-from-mongodb)