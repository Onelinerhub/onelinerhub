# How to use eq in MongoDB?
// plain

MongoDB's `$eq` operator is used to match values that are equal to a specified value. It is part of the MongoDB query language and can be used in the `find()` method.

## Example

```
db.collection.find({ field: { $eq: value } })
```

This example will return all documents in the collection where the value of the `field` field is equal to `value`.

## Code explanation

- `$eq`: The MongoDB operator used to match values that are equal to a specified value.
- `find()`: The MongoDB method used to query documents in a collection.
- `field`: The field in the document to query.
- `value`: The value to match against the field.

## Helpful links
- [MongoDB Query Operators](https://docs.mongodb.com/manual/reference/operator/query/)
- [MongoDB find() Method](https://docs.mongodb.com/manual/reference/method/db.collection.find/)

onelinerhub: [How to use eq in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-eq-in-mongodb)