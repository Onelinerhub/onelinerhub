# How to count aggregated results in MongoDB?
// plain

MongoDB provides the `$group` aggregation operator to group documents by a specified key and apply accumulator expressions. The `$group` operator can be used to count the number of documents in a collection or the number of documents that match a specific criteria.

## Example code

```
db.collection.aggregate([
    {
        $group: {
            _id: null,
            count: { $sum: 1 }
        }
    }
])
```

## Output example

```
{ "_id" : null, "count" : 5 }
```

## Code explanation

- `$group`: This is the aggregation operator used to group documents by a specified key.
- `_id`: This is the field used to specify the key to group documents by. In this example, `_id` is set to `null` to group all documents together.
- `count`: This is the field used to store the result of the accumulator expression.
- `$sum`: This is the accumulator expression used to count the number of documents.

## Helpful links
- [MongoDB Aggregation](https://docs.mongodb.com/manual/aggregation/)
- [MongoDB $group](https://docs.mongodb.com/manual/reference/operator/aggregation/group/)

onelinerhub: [How to count aggregated results in MongoDB?](https://onelinerhub.com/mongodb/how-to-count-aggregated-results-in-mongodb)