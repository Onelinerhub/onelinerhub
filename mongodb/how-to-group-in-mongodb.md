# How to group in MongoDB?
// plain

MongoDB provides the `$group` aggregation operator to group documents by a specified key and perform accumulator operations.

## Example

```
db.collection.aggregate([
    {
        $group: {
            _id: "$department",
            totalSalary: { $sum: "$salary" }
        }
    }
])
```
## Output example

```
{ "_id" : "IT", "totalSalary" : 30000 }
{ "_id" : "HR", "totalSalary" : 15000 }
```

The `$group` operator has the following parts:

- `_id`: The key to group documents by.
- `totalSalary`: The accumulator expression to perform operations on the grouped documents.

## Helpful links
- [MongoDB Aggregation](https://docs.mongodb.com/manual/aggregation/)

onelinerhub: [How to group in MongoDB?](https://onelinerhub.com/mongodb/how-to-group-in-mongodb)