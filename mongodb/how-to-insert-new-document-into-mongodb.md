# How to insert new document into MongoDB?
// plain

To insert a new document into MongoDB, use the `insertOne()` method. This method takes two parameters: a document object and an optional options object.

## Example

```
db.collection.insertOne({
    name: "John Doe",
    age: 25
});
```
## Output example

```
{
    "acknowledged" : true,
    "insertedId" : ObjectId("5f3f9f9f9f9f9f9f9f9f9f9f")
}
```

## Code explanation

- `insertOne()`: The method used to insert a new document into MongoDB.
- `{name: "John Doe", age: 25}`: The document object containing the data to be inserted.
- `options`: An optional parameter that can be used to specify additional options for the operation.

## Helpful links
- [MongoDB Documentation - insertOne()](https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/)

onelinerhub: [How to insert new document into MongoDB?](https://onelinerhub.com/mongodb/how-to-insert-new-document-into-mongodb)