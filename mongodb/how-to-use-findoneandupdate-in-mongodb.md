# How to use findoneandupdate in MongoDB?
// plain

MongoDB's `findOneAndUpdate()` method is used to find a single document and update it. It takes a filter, an update, and an optional options document as arguments. The filter is used to select the document to update, the update is used to specify the modifications to be made, and the options document can be used to specify additional options such as the sort order.

## Example

```
db.collection.findOneAndUpdate(
   <filter>,
   <update>,
   {
     upsert: <boolean>,
     returnOriginal: <boolean>,
     sort: <document>,
     projection: <document>,
     maxTimeMS: <number>,
     ...
   }
)
```

## Output example

```
{
   "_id" : ObjectId("5f3d2f8a7f8ea6d7f8b2d8fe"),
   "name" : "John Doe",
   "age" : 25,
   "status" : "A"
}
```

## Code explanation

- `<filter>`: A document that specifies the criteria for selecting the document to update.
- `<update>`: A document that specifies the modifications to be made to the document.
- `upsert`: A boolean that specifies whether to insert a new document if no document matches the filter.
- `returnOriginal`: A boolean that specifies whether to return the original document or the updated document.
- `sort`: A document that specifies the sort order for the query.
- `projection`: A document that specifies the fields to return.
- `maxTimeMS`: A number that specifies the maximum amount of time to allow the query to run.

## Helpful links
- [MongoDB Documentation - findOneAndUpdate()](https://docs.mongodb.com/manual/reference/method/db.collection.findOneAndUpdate/)

onelinerhub: [How to use findoneandupdate in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-findoneandupdate-in-mongodb)