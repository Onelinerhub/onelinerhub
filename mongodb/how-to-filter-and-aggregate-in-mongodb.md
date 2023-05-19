# How to filter and aggregate in MongoDB?
// plain

MongoDB provides powerful aggregation and filtering capabilities. Aggregation operations group values from multiple documents together, and can perform a variety of operations on the grouped data to return a single result. Filtering operations allow documents to be filtered so that only those documents that match the specified criteria are returned.

## Example code

```
db.collection.aggregate([
  {
    $match: {
      age: { $gt: 18 }
    }
  },
  {
    $group: {
      _id: null,
      avgAge: { $avg: "$age" }
    }
  }
])
```

## Output example

```
{ "_id" : null, "avgAge" : 25.5 }
```

## Code explanation

- `$match`: This is a filtering operation that allows documents to be filtered so that only those documents that match the specified criteria are returned. In this example, only documents with an age greater than 18 are returned.
- `$group`: This is an aggregation operation that groups values from multiple documents together. In this example, all documents with an age greater than 18 are grouped together and the average age is calculated.

## Helpful links
- [MongoDB Aggregation](https://docs.mongodb.com/manual/aggregation/)
- [MongoDB Filtering](https://docs.mongodb.com/manual/tutorial/query-documents/)

onelinerhub: [How to filter and aggregate in MongoDB?](https://onelinerhub.com/mongodb/how-to-filter-and-aggregate-in-mongodb)