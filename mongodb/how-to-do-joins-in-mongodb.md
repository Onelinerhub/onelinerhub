# How to do joins in MongoDB?
// plain

MongoDB supports various types of joins to combine documents from multiple collections. The most commonly used join is the `$lookup` operator. It performs a left outer join to an unsharded collection in the same database to filter in documents from the “joined” collection for processing.

```
db.collection.aggregate([
  {
    $lookup:
      {
        from: "otherCollection",
        localField: "field1",
        foreignField: "field2",
        as: "alias_name"
      }
   }
])
```

The above example code performs a `$lookup` operation on the `collection` collection, joining documents from the `otherCollection` collection. The `localField` and `foreignField` parameters specify the fields used to match documents from the two collections. The `as` parameter specifies the name of the new array field in the input documents.

Other join operations supported by MongoDB include `$merge`, `$graphLookup`, `$facet`, and `$unwind`.

## Helpful links

- [MongoDB Documentation - Joins](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/)
- [MongoDB Documentation - $lookup](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/)
- [MongoDB Documentation - $merge](https://docs.mongodb.com/manual/reference/operator/aggregation/merge/)
- [MongoDB Documentation - $graphLookup](https://docs.mongodb.com/manual/reference/operator/aggregation/graphLookup/)
- [MongoDB Documentation - $facet](https://docs.mongodb.com/manual/reference/operator/aggregation/facet/)
- [MongoDB Documentation - $unwind](https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/)

onelinerhub: [How to do joins in MongoDB?](https://onelinerhub.com/mongodb/how-to-do-joins-in-mongodb)