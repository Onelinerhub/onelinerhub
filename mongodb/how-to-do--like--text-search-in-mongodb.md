# How to do "like" text search in MongoDB?
// plain

MongoDB provides a powerful text search feature that allows you to perform "like" text searches. To do this, you need to create a text index on the collection that you want to search. This can be done using the `createIndex()` method.

```
db.collection.createIndex( { "$**": "text" } )
```

This will create a text index on all fields in the collection. Once the index is created, you can perform a text search using the `$text` operator.

```
db.collection.find( { $text: { $search: "like text" } } )
```

This will return all documents that contain the phrase "like text".

## Code explanation


1. `createIndex()` method: used to create a text index on the collection.
2. `$text` operator: used to perform a text search.
3. `$search` parameter: used to specify the search phrase.

## Helpful links

- [MongoDB Text Search](https://docs.mongodb.com/manual/text-search/)

onelinerhub: [How to do "like" text search in MongoDB?](https://onelinerhub.com/mongodb/how-to-do--like--text-search-in-mongodb)