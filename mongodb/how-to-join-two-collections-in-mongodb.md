# How to join two collections in MongoDB?
// plain

MongoDB provides the `$lookup` operator to join two collections. This operator takes two parameters, `from` and `localField`. `from` specifies the collection to join with and `localField` specifies the field from the current collection to match with the `from` collection.

## Example

```
db.collection1.aggregate([
    {
        $lookup:
        {
            from: "collection2",
            localField: "field1",
            foreignField: "field2",
            as: "joined_data"
        }
    }
])
```

## Output example

```
{
    "_id" : ObjectId("5f3d7f9f8f8d7f3d7f9f8d7"),
    "field1" : "value1",
    "joined_data" : [
        {
            "_id" : ObjectId("5f3d7f9f8f8d7f3d7f9f8d7"),
            "field2" : "value1",
            "other_field" : "value2"
        }
    ]
}
```

## Code explanation

- `$lookup`: The MongoDB operator used to join two collections.
- `from`: The collection to join with.
- `localField`: The field from the current collection to match with the `from` collection.
- `foreignField`: The field from the `from` collection to match with the current collection.
- `as`: The name of the new array field to add to the documents.

## Helpful links
- [MongoDB Documentation - $lookup](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/)

onelinerhub: [How to join two collections in MongoDB?](https://onelinerhub.com/mongodb/how-to-join-two-collections-in-mongodb)