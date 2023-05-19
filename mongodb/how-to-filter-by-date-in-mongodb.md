# How to filter by date in MongoDB?
// plain

MongoDB provides a range of operators to filter documents by date. The most commonly used operators are `$gt` (greater than), `$gte` (greater than or equal to), `$lt` (less than) and `$lte` (less than or equal to).

For example, to filter documents with a date field `createdAt` greater than a given date, the following code can be used:

```
db.collection.find({
  createdAt: {
    $gt: new Date("2020-01-01")
  }
})
```

This will return all documents with a `createdAt` field greater than `2020-01-01`.

## Code explanation


- `db.collection.find()`: This is the MongoDB command to query documents from a collection.
- `createdAt`: This is the name of the date field in the documents.
- `$gt`: This is the operator used to filter documents with a date field greater than a given date.
- `new Date("2020-01-01")`: This is the given date used for comparison.

## Helpful links

- [MongoDB Query Operators](https://docs.mongodb.com/manual/reference/operator/query/)

onelinerhub: [How to filter by date in MongoDB?](https://onelinerhub.com/mongodb/how-to-filter-by-date-in-mongodb)