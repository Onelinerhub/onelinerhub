# How to map in MongoDB?
// plain

MongoDB provides a powerful way to store and query data using its document-oriented data model. To map data in MongoDB, you can use the `db.collection.insert()` method to insert documents into a collection. The documents can be structured in any way you like, and you can use the `$set` operator to update existing documents.

## Example code

```
db.collection.insert({
  name: "John Doe",
  age: 25
});

db.collection.update({
  name: "John Doe"
}, {
  $set: {
    age: 26
  }
});
```

## Output example

```
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

## Code explanation


1. `db.collection.insert()`: This method is used to insert documents into a collection. The documents can be structured in any way you like.
2. `$set`: This operator is used to update existing documents. It takes a field name and a value as parameters.

## Helpful links

- [MongoDB Documentation](https://docs.mongodb.com/)
- [MongoDB Tutorial](https://www.tutorialspoint.com/mongodb/)

onelinerhub: [How to map in MongoDB?](https://onelinerhub.com/mongodb/how-to-map-in-mongodb)