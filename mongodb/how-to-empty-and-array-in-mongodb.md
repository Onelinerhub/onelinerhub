# How to empty and array in MongoDB?
// plain

To empty an array in MongoDB, you can use the `$unset` operator. This operator will remove the specified field from the document.

For example, to empty the `tags` array in the document `{ _id: 1, tags: ["a", "b", "c"] }`, you can use the following command:
```
db.collection.update({ _id: 1 }, { $unset: { tags: "" } })
```

The command above will result in the following document:
```
{ _id: 1 }
```

The command consists of the following parts:
- `db.collection.update`: This is the command used to update a document in MongoDB.
- `{ _id: 1 }`: This is the filter used to identify the document to be updated.
- `{ $unset: { tags: "" } }`: This is the update operator used to remove the `tags` field from the document.

## Helpful links
- [MongoDB Documentation - $unset](https://docs.mongodb.com/manual/reference/operator/update/unset/)

onelinerhub: [How to empty and array in MongoDB?](https://onelinerhub.com/mongodb/how-to-empty-and-array-in-mongodb)