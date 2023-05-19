# How to drop a collection in MongoDB?
// plain

To drop a collection in MongoDB, use the `drop()` method. This method will delete the specified collection from the current database.

## Example

```
db.collection.drop()
```

## Output example

```
true
```

The `drop()` method takes no arguments and returns `true` if the collection was dropped successfully, or `false` if the collection does not exist.

## Code explanation

- `db`: The database object.
- `collection`: The name of the collection to be dropped.
- `drop()`: The method used to drop the collection.

## Helpful links
- [MongoDB Documentation - drop()](https://docs.mongodb.com/manual/reference/method/db.collection.drop/)

onelinerhub: [How to drop a collection in MongoDB?](https://onelinerhub.com/mongodb/how-to-drop-a-collection-in-mongodb)