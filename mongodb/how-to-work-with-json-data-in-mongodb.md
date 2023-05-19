# How to work with JSON data in MongoDB?
// plain

MongoDB provides a native JSON data type that allows developers to store and query JSON documents directly in the database. To work with JSON data in MongoDB, you can use the `$jsonSchema` operator to validate the structure of the documents. Additionally, you can use the `$jsonArray` operator to query for specific elements in an array.

## Example code

```
db.collection.find({
  $jsonSchema: {
    bsonType: "object",
    required: ["name", "age"],
    properties: {
      name: {
        bsonType: "string",
        description: "must be a string and is required"
      },
      age: {
        bsonType: "int",
        minimum: 0,
        description: "must be an integer and is required"
      }
    }
  }
})
```

## Output example

```
{ "_id" : ObjectId("5f3f9f9f9f9f9f9f9f9f9f9f"), "name" : "John", "age" : 30 }
```

## Code explanation

- `$jsonSchema` operator: This operator is used to validate the structure of the documents.
- `bsonType`: This is used to specify the type of data that is expected in the document.
- `required`: This is used to specify which fields are required in the document.
- `properties`: This is used to specify the properties of the document.

## Helpful links
- [MongoDB Documentation - Working with JSON](https://docs.mongodb.com/manual/reference/operator/query/jsonSchema/)

onelinerhub: [How to work with JSON data in MongoDB?](https://onelinerhub.com/mongodb/how-to-work-with-json-data-in-mongodb)