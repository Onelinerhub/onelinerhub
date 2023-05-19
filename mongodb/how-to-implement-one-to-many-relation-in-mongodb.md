# How to implement one-to-many relation in MongoDB?
// plain

MongoDB supports one-to-many relationships using the `$lookup` operator. This operator allows you to join two collections together and return the matching documents from both collections.

For example, the following code will join the `orders` collection with the `products` collection and return the matching documents:

```
db.orders.aggregate([
    {
        $lookup:
        {
            from: "products",
            localField: "productId",
            foreignField: "_id",
            as: "products"
        }
    }
])
```

The code above will return the following output:

```
{
    "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"),
    "productId" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"),
    "products" : [
        {
            "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"),
            "name" : "Product 1",
            "price" : 10
        }
    ]
}
```

## Code explanation


1. `$lookup` - This is the operator used to join two collections.
2. `from` - This is the collection to join with.
3. `localField` - This is the field in the current collection to match with the foreignField.
4. `foreignField` - This is the field in the foreign collection to match with the localField.
5. `as` - This is the name of the array field that will contain the matching documents from the foreign collection.

## Helpful links

- [MongoDB Documentation - $lookup](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/)

onelinerhub: [How to implement one-to-many relation in MongoDB?](https://onelinerhub.com/mongodb/how-to-implement-one-to-many-relation-in-mongodb)