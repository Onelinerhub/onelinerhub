# How to check if array is empty in MongoDB?
// plain

To check if an array is empty in MongoDB, you can use the `$size` operator. This operator returns the number of elements in an array. If the array is empty, the `$size` operator will return 0.

## Example code

```
db.collection.find( { arrayField: { $size: 0 } } )
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "arrayField" : [] }
```

## Code explanation

- `db.collection.find()`: This is the MongoDB command to query a collection.
- `{ arrayField: { $size: 0 } }`: This is the query condition to check if the array is empty. The `$size` operator returns the number of elements in an array. If the array is empty, the `$size` operator will return 0.

## Helpful links
- [MongoDB Documentation - $size](https://docs.mongodb.com/manual/reference/operator/query/size/)

onelinerhub: [How to check if array is empty in MongoDB?](https://onelinerhub.com/mongodb/how-to-check-if-array-is-empty-in-mongodb)