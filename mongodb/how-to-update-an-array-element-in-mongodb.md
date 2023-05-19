# How to update an array element in MongoDB?
// plain

Updating an array element in MongoDB can be done using the `$set` operator. The `$set` operator is used to specify the element in an array to update.

## Example

```
db.collection.update(
   { _id: 1 },
   { $set: { "array.$[element].name": "updated" } }
)
```

## Output example

```
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

The code above updates the `name` field of the element in the `array` array that matches the `element` condition.

## Code explanation

- `db.collection.update`: This is the MongoDB command used to update a document.
- `{ _id: 1 }`: This is the condition used to identify the document to update.
- `{ $set: { "array.$[element].name": "updated" } }`: This is the update operator used to update the `name` field of the element in the `array` array that matches the `element` condition.

## Helpful links
- [MongoDB Update Operators](https://docs.mongodb.com/manual/reference/operator/update/)

onelinerhub: [How to update an array element in MongoDB?](https://onelinerhub.com/mongodb/how-to-update-an-array-element-in-mongodb)