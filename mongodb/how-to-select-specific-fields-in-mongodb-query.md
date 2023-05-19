# How to select specific fields in MongoDB query?
// plain

MongoDB provides the `$project` operator to select specific fields in a query. The `$project` operator takes a document that specifies the fields to include or exclude.

## Example

```
db.collection.find({}, {name: 1, age: 1})
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "John", "age" : 25 }
```

The code above will select the `name` and `age` fields from the collection.

## Code explanation


- `db.collection.find({}, {name: 1, age: 1})`: This is the MongoDB query that will select the `name` and `age` fields from the collection.
- `{}`: This is an empty document that specifies that all documents in the collection should be selected.
- `name: 1`: This specifies that the `name` field should be included in the query.
- `age: 1`: This specifies that the `age` field should be included in the query.

## Helpful links

- [MongoDB Documentation - Projection Operators](https://docs.mongodb.com/manual/reference/operator/projection/)

onelinerhub: [How to select specific fields in MongoDB query?](https://onelinerhub.com/mongodb/how-to-select-specific-fields-in-mongodb-query)