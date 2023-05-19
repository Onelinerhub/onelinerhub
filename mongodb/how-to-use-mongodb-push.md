# How to use MongoDB push?
// plain

MongoDB push is a method used to add new elements to an array field in a MongoDB document. It is used to add elements to the end of an array.

## Example code

```
db.collection.update(
   { _id: 1 },
   { $push: { array_field: "new_element" } }
)
```

## Output example

```
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

## Code explanation

- `db.collection.update`: This is the MongoDB command used to update a document in a collection.
- `{ _id: 1 }`: This is the filter used to identify the document to be updated.
- `{ $push: { array_field: "new_element" } }`: This is the update operator used to add a new element to the end of an array field.
- `WriteResult`: This is the output of the command, indicating that the document was successfully updated.

## Helpful links
- [MongoDB Documentation - $push](https://docs.mongodb.com/manual/reference/operator/update/push/)

onelinerhub: [How to use MongoDB push?](https://onelinerhub.com/mongodb/how-to-use-mongodb-push)