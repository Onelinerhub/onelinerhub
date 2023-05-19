# How to find by id in MongoDB?
// plain

To find a document by its id in MongoDB, you can use the `findOne()` method. This method takes a query object as its first argument and returns the first document that matches the query.

## Example code

```
db.collection.findOne({ _id: ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f") });
```

## Output example

```
{
  _id: ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f"),
  name: "John Doe",
  age: 30
}
```

## Code explanation

- `db.collection.findOne()`: This is the method used to find a document by its id.
- `{ _id: ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f") }`: This is the query object used to find the document. The `_id` field is used to specify the id of the document to be found.
- `ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f")`: This is the id of the document to be found.

## Helpful links
- [MongoDB Documentation - findOne()](https://docs.mongodb.com/manual/reference/method/db.collection.findOne/)

onelinerhub: [How to find by id in MongoDB?](https://onelinerhub.com/mongodb/how-to-find-by-id-in-mongodb)