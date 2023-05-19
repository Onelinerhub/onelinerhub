# How to use unwind in MongoDB?
// plain

Unwind is an operator in MongoDB that allows you to deconstruct an array field from the input documents to output a document for each element in the array.

## Example

```
db.collection.aggregate([
    {
        $unwind: "$arrayField"
    }
])
```

## Output example

```
{ _id: 1, arrayField: "a" }
{ _id: 1, arrayField: "b" }
{ _id: 1, arrayField: "c" }
```

## Code explanation

- `$unwind`: the operator used to deconstruct the array field
- `arrayField`: the array field to be deconstructed

## Helpful links
- [MongoDB Unwind Operator](https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/)

onelinerhub: [How to use unwind in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-unwind-in-mongodb)