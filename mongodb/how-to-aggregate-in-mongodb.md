# How to aggregate in MongoDB?
// plain

MongoDB provides several ways to aggregate data from collections. The most common way is to use the `aggregate()` method. This method takes an array of pipeline stages as its argument and returns the aggregated result.

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
{ "_id" : "IT", "totalSalary" : 15000 }
{ "_id" : "HR", "totalSalary" : 12000 }
```

## Code explanation

- `aggregate()`: The method used to aggregate data from collections.
- `$group`: The operator used to group documents by a specified field and perform an aggregation on them.
- `_id`: The field used to specify the field to group by.
- `$sum`: The operator used to sum the values of a specified field.

## Helpful links
- [MongoDB Aggregation](https://docs.mongodb.com/manual/aggregation/)

onelinerhub: [How to aggregate in MongoDB?](https://onelinerhub.com/mongodb/how-to-aggregate-in-mongodb)