# How to use elemmatch in MongoDB?
// plain

Elemmatch is a MongoDB query operator used to match a specific element in an array. It is used to match a single element in an array that meets the specified criteria.

## Example

```
db.collection.find( { arrayField: { $elemMatch: { <element1>: <value1>, <element2>: <value2>, ... } } } )
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "arrayField" : [ { <element1> : <value1>, <element2> : <value2>, ... }, { <element1> : <value3>, <element2> : <value4>, ... }, ... ] }
```

## Code explanation


1. `db.collection.find()`: This is the MongoDB command used to query a collection.

2. `{ arrayField: { $elemMatch: { <element1>: <value1>, <element2>: <value2>, ... } } }`: This is the query criteria used to match a single element in an array that meets the specified criteria. The `$elemMatch` operator is used to match a specific element in an array. The `<element1>` and `<element2>` are the fields in the array that need to be matched, and `<value1>` and `<value2>` are the values that need to be matched.

## Helpful links

- [MongoDB Documentation - $elemMatch](https://docs.mongodb.com/manual/reference/operator/query/elemMatch/)

onelinerhub: [How to use elemmatch in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-elemmatch-in-mongodb)