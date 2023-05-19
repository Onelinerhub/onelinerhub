# How to use insertone in MongoDB?
// plain

MongoDB's `insertOne()` method is used to insert a single document into a collection.

## Example

```
db.collection.insertOne(
   {
      item: "canvas",
      qty: 100,
      tags: ["cotton"],
      size: { h: 28, w: 35.5, uom: "cm" }
   }
)
```

## Output example

```
{
	"acknowledged" : true,
	"insertedId" : ObjectId("5f3d7f9f8f9f8f9f8f9f8f9f")
}
```

## Code explanation

- `db.collection.insertOne()`: This is the method used to insert a single document into a collection.
- `{ item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }`: This is the document that is being inserted into the collection.
- `acknowledged`: This is a boolean value that indicates whether the operation was successful or not.
- `insertedId`: This is the unique identifier of the document that was inserted.

## Helpful links
- [MongoDB Documentation - insertOne()](https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/)

onelinerhub: [How to use insertone in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-insertone-in-mongodb)