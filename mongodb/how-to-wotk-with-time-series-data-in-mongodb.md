# How to work with time series data in MongoDB?
// plain

MongoDB is a great choice for working with time series data. It provides a powerful aggregation framework that allows you to quickly analyze and visualize your data. To work with time series data in MongoDB, you can use the `$dateToString` operator to convert dates to strings, and the `$group` operator to group documents by time intervals.

## Example code

```
db.collection.aggregate([
  {
    $group: {
      _id: {
        $dateToString: {
          format: "%Y-%m-%d",
          date: "$date"
        }
      },
      count: { $sum: 1 }
    }
  }
])
```

## Output example

```
{ "_id" : "2020-01-01", "count" : 2 }
{ "_id" : "2020-01-02", "count" : 3 }
{ "_id" : "2020-01-03", "count" : 1 }
```

## Code explanation


1. `$dateToString`: This operator converts a date to a string using the specified format. In this example, the date is converted to a string in the format of `YYYY-MM-DD`.
2. `$group`: This operator groups documents by the specified _id field. In this example, the documents are grouped by the date string created by the `$dateToString` operator.
3. `$sum`: This operator sums up the values of the specified field. In this example, the `count` field is incremented by 1 for each document in the group.

## Helpful links

- [MongoDB Aggregation Framework](https://docs.mongodb.com/manual/aggregation/)
- [MongoDB Date Operators](https://docs.mongodb.com/manual/reference/operator/aggregation/dateToString/)

onelinerhub: [How to wotk with time series data in MongoDB?
](https://onelinerhub.com/mongodb/how-to-wotk-with-time-series-data-in-mongodb)
