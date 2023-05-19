# How to sort MongoDB query results?
// plain

MongoDB provides a `sort()` method to sort query results. The `sort()` method takes a document as its argument, which contains the field or fields to sort by and the sort order.

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

The `sort()` method takes a document as its argument, which contains the field or fields to sort by and the sort order. The field or fields to sort by is specified by the `key` and the sort order is specified by the `value`:

- `1`: ascending order
- `-1`: descending order

## Code explanation


- `db.collection.find()`: This is the MongoDB query to find documents in a collection.

- `.sort({name: 1})`: This is the `sort()` method, which takes a document as its argument. The document contains the field or fields to sort by (`name`) and the sort order (`1` for ascending order).

## Helpful links

- [MongoDB Documentation - sort()](https://docs.mongodb.com/manual/reference/method/cursor.sort/)

onelinerhub: [How to sort MongoDB query results?](https://onelinerhub.com/mongodb/how-to-sort-mongodb-query-results)