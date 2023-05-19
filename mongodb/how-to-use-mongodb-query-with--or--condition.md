# How to use MongoDB query with "or" condition?
// plain

MongoDB query with "or" condition can be used to query multiple conditions in a single query. The syntax for this is `$or` followed by an array of conditions.

## Example code

```
db.collection.find({
  $or: [
    { condition1 },
    { condition2 }
  ]
})
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "John", "age" : 25 }
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "Jane", "age" : 30 }
```

## Code explanation


- `$or`: This is the operator used to specify multiple conditions in a single query.
- `[ ]`: This is an array of conditions that will be evaluated.
- `condition1` and `condition2`: These are the conditions that will be evaluated.

## Helpful links

- [MongoDB Documentation - $or](https://docs.mongodb.com/manual/reference/operator/query/or/)

onelinerhub: [How to use MongoDB query with "or" condition?](https://onelinerhub.com/mongodb/how-to-use-mongodb-query-with--or--condition)