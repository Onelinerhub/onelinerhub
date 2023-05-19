# How to get all documents in MongoDB?
// plain

To get all documents in MongoDB, you can use the `find()` method. This method returns a cursor object which can be iterated over to get all documents in a collection.

## Example code

```
db.collection.find()
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f"), "name" : "John", "age" : 25 }
{ "_id" : ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f"), "name" : "Jane", "age" : 30 }
```

## Code explanation

- `db.collection.find()`: This is the syntax for the `find()` method. It takes an optional parameter which is a query object to filter the documents.
- `ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f")`: This is the unique identifier for each document in MongoDB.

## Helpful links
- [MongoDB Documentation - find()](https://docs.mongodb.com/manual/reference/method/db.collection.find/)

onelinerhub: [How to get all documents in MongoDB?](https://onelinerhub.com/mongodb/how-to-get-all-documents-in-mongodb)