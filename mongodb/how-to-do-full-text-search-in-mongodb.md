# How to do full text search in MongoDB?
// plain

MongoDB provides a text search feature that allows users to perform full text search on string content. This feature is available in MongoDB versions 2.4 and higher.

To perform a full text search, the `$text` operator can be used in a `find()` query. The `$text` operator takes a search string as an argument and returns documents that contain the specified string.

## Example

```
db.collection.find( { $text: { $search: "coffee" } } )
```

## Output example

```
{ "_id" : ObjectId("5f3d7f9f8f9f9f9f9f9f9f9f"), "name" : "Coffee Maker", "description" : "This is a coffee maker." }
```

The `$text` operator can also be used with other operators such as `$and`, `$or`, and `$not` to create more complex search queries.

## Helpful links
- [MongoDB Text Search](https://docs.mongodb.com/manual/text-search/)
- [MongoDB Query Operators](https://docs.mongodb.com/manual/reference/operator/query/)

onelinerhub: [How to do full text search in MongoDB?](https://onelinerhub.com/mongodb/how-to-do-full-text-search-in-mongodb)