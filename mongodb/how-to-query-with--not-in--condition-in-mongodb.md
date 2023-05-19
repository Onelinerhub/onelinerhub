# How to query with "not in" condition in MongoDB?
// plain

MongoDB provides the `$nin` operator to query documents with a "not in" condition. The `$nin` operator is used to specify a query condition to select documents that do not match the specified values.

## Example

```
db.collection.find({
  field: {
    $nin: [value1, value2, ...]
  }
})
```

This example will return all documents in the collection where the value of the field is not equal to any of the specified values.

Parts of the code:
- `db.collection.find()`: This is the MongoDB query method used to find documents in a collection.
- `field`: This is the name of the field in the document that is being queried.
- `$nin`: This is the MongoDB operator used to specify a "not in" condition.
- `[value1, value2, ...]`: This is an array of values that the field must not match.

## Helpful links
- [MongoDB Query Operators](https://docs.mongodb.com/manual/reference/operator/query/)

onelinerhub: [How to query with "not in" condition in MongoDB?](https://onelinerhub.com/mongodb/how-to-query-with--not-in--condition-in-mongodb)