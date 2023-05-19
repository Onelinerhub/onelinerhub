# How to order query results in MongoDB?
// plain

MongoDB provides the `sort()` method to order query results. The `sort()` method takes a document as an argument, which contains the field or fields to sort by and the sort order.

## Example

```
db.collection.find().sort({name: 1})
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "Alice" }
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "Bob" }
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "John" }
```

## Code explanation


- `db.collection.find()`: This is the command to query the collection.
- `sort({name: 1})`: This is the command to sort the query results. The `name` field is the field to sort by, and `1` is the sort order (ascending).

## Helpful links

- [MongoDB Documentation - sort()](https://docs.mongodb.com/manual/reference/method/cursor.sort/)

onelinerhub: [How to order query results in MongoDB?](https://onelinerhub.com/mongodb/how-to-order-query-results-in-mongodb)