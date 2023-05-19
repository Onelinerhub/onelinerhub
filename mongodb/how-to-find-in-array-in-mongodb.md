# How to find in array in MongoDB?
// plain

MongoDB provides a powerful `$elemMatch` operator to query array elements. This operator can be used to match a single element or multiple elements of an array.

## Example

```
db.collection.find(
   { arrayField: { $elemMatch: { <query1>, <query2>, ... } } }
)
```

This example will return documents where the arrayField contains at least one element that matches all the query criteria.

## Code explanation


1. `db.collection.find` - This is the MongoDB command to query a collection.
2. `{ arrayField: { $elemMatch: { <query1>, <query2>, ... } } }` - This is the query criteria to match array elements. `arrayField` is the name of the array field, `$elemMatch` is the operator to match array elements, and `<query1>, <query2>, ...` are the query criteria for the array elements.

## Helpful links

- [MongoDB Documentation - Query an Array](https://docs.mongodb.com/manual/tutorial/query-arrays/)

onelinerhub: [How to find in array in MongoDB?](https://onelinerhub.com/mongodb/how-to-find-in-array-in-mongodb)