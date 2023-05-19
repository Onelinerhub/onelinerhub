# How to check if a document exists in MongoDB?
// plain

To check if a document exists in MongoDB, you can use the `findOne()` method. This method returns the first document that matches the query criteria.

## Example

```
db.collection.findOne({name: "John"})
```

## Output example

```
{
    "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"),
    "name" : "John",
    "age" : 25
}
```

## Code explanation

- `db.collection`: specifies the collection to query
- `findOne()`: method to query the collection
- `{name: "John"}`: query criteria

## Helpful links
- [MongoDB Documentation - findOne()](https://docs.mongodb.com/manual/reference/method/db.collection.findOne/)

onelinerhub: [How to check if a document exists in MongoDB?](https://onelinerhub.com/mongodb/how-to-check-if-a-document-exists-in-mongodb)