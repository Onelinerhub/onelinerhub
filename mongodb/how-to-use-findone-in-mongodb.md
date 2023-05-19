# How to use findone in MongoDB?
// plain

MongoDB's `findOne()` method is used to query a collection and return a single document that matches the specified query criteria.

## Example

```
db.collection.findOne({name: "John"})
```
## Output example

```
{
  "_id": ObjectId("5f3d7f8d3f9f8d7f8d7f8d7f"),
  "name": "John",
  "age": 25
}
```

## Code explanation

- `db.collection`: specifies the collection to query
- `findOne()`: the method used to query the collection
- `{name: "John"}`: the query criteria, in this case, the document must have a `name` field with the value `John`

## Helpful links
- [MongoDB Documentation - findOne()](https://docs.mongodb.com/manual/reference/method/db.collection.findOne/)

onelinerhub: [How to use findone in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-findone-in-mongodb)