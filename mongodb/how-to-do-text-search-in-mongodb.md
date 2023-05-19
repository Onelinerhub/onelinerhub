# How to do text search in MongoDB?
// plain

Text search in MongoDB can be done using the `$text` operator. This operator allows for a full-text search of string content in a collection.

## Example code

```
db.collection.find({$text: {$search: "text to search"}})
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "John Doe", "text" : "This is some text to search" }
```

## Code explanation

- `db.collection.find()`: This is the MongoDB command to query a collection.
- `$text`: This is the MongoDB operator used to perform a full-text search.
- `$search`: This is the parameter used to specify the text to search for.

## Helpful links
- [MongoDB Text Search](https://docs.mongodb.com/manual/text-search/)

onelinerhub: [How to do text search in MongoDB?](https://onelinerhub.com/mongodb/how-to-do-text-search-in-mongodb)