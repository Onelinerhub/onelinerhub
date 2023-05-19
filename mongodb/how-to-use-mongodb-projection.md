# How to use MongoDB projection?
// plain

MongoDB projection is used to select only the required fields from a document. It is done by passing a projection document to the `find()` method. The projection document specifies the fields to be returned in the result set.

## Example

```
db.collection.find({}, {name: 1, age: 1})
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "John", "age" : 25 }
```

## Code explanation

- `db.collection.find()`: This is the method used to query the collection.
- `{}`: This is the filter document used to specify the criteria for the query.
- `{name: 1, age: 1}`: This is the projection document used to specify the fields to be returned in the result set.

## Helpful links
- [MongoDB Documentation - Projection](https://docs.mongodb.com/manual/tutorial/project-fields-from-query-results/)

onelinerhub: [How to use MongoDB projection?](https://onelinerhub.com/mongodb/how-to-use-mongodb-projection)