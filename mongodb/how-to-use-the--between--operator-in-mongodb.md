# How to use the "between" operator in MongoDB?
// plain

The `$between` operator in MongoDB is used to specify a range of values for a given field. It is used to select documents where the value of the field is greater than or equal to the specified lower bound and less than or equal to the specified upper bound.

## Example

```
db.collection.find({
  field: {
    $between: [lowerBound, upperBound]
  }
})
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "field" : 10 }
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "field" : 15 }
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "field" : 20 }
```

## Code explanation

- `db.collection.find()`: This is the method used to query the collection.
- `field`: This is the field in the collection that is being queried.
- `$between`: This is the operator used to specify a range of values for the given field.
- `lowerBound`: This is the lower bound of the range of values.
- `upperBound`: This is the upper bound of the range of values.

## Helpful links
- [MongoDB Documentation - $between](https://docs.mongodb.com/manual/reference/operator/query/between/)

onelinerhub: [How to use the "between" operator in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-the--between--operator-in-mongodb)