# How to use MongoDB pull?
// plain

MongoDB's `$pull` operator is used to remove an item from an array. It takes two arguments: the first is the name of the field containing the array, and the second is the value to be removed.

## Example

```
db.collection.update(
   { _id: 1 },
   { $pull: { arrayField: "valueToRemove" } }
)
```

## Output example

```
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

## Code explanation

- `db.collection.update`: This is the MongoDB command used to update a document in a collection.
- `{ _id: 1 }`: This is the query used to select the document to update.
- `{ $pull: { arrayField: "valueToRemove" } }`: This is the update operator used to remove an item from an array. The first argument is the name of the field containing the array, and the second is the value to be removed.

## Helpful links
- [MongoDB Documentation - $pull](https://docs.mongodb.com/manual/reference/operator/update/pull/)

onelinerhub: [How to use MongoDB pull?](https://onelinerhub.com/mongodb/how-to-use-mongodb-pull)