# How to query with "not equal" condition in MongoDB?
// plain

MongoDB provides the `$ne` operator to query documents with "not equal" condition. The `$ne` operator matches all the documents that do not contain the specified field value.

## Example

```
db.collection.find({ field: { $ne: value } })
```

This example will return all documents in the collection where the value of the field does not equal the specified value.

## Code explanation

- `db.collection.find()`: This is the MongoDB query method used to find documents in a collection.
- `{ field: { $ne: value } }`: This is the query condition used to specify the field and value to match. The `$ne` operator is used to match documents where the field does not equal the specified value.

## Helpful links
- [MongoDB Query Operators](https://docs.mongodb.com/manual/reference/operator/query/)

onelinerhub: [How to query with "not equal" condition in MongoDB?](https://onelinerhub.com/mongodb/how-to-query-with--not-equal--condition-in-mongodb)