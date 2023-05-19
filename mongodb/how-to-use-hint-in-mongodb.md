# How to use hint in MongoDB?
// plain

Hints in MongoDB are used to provide the query optimizer with additional information about the query. This can help the query optimizer to choose the most efficient query plan.

## Example

```
db.collection.find({name: "John"}).hint({name: 1})
```

This example will use the index on the `name` field to find documents with the name "John".

## Code explanation


1. `db.collection.find({name: "John"})` - This is the query that will be used to find documents with the name "John".
2. `.hint({name: 1})` - This is the hint that will be used to provide the query optimizer with additional information about the query.
3. `name: 1` - This is the index that will be used to find documents with the name "John".

## Helpful links

- [MongoDB Documentation - Hint](https://docs.mongodb.com/manual/reference/method/db.collection.find/#hint)

onelinerhub: [How to use hint in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-hint-in-mongodb)