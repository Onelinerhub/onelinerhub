# How to clear a collection in MongoDB?
// plain

To clear a collection in MongoDB, you can use the `drop()` method. This will delete the collection and all of its documents.

## Example

```
db.collection.drop()
```

## Output example

```
true
```

The `drop()` method takes no parameters and returns true if the collection was dropped successfully.

## Code explanation

- `db`: This is the database object.
- `collection`: This is the name of the collection to be dropped.
- `drop()`: This is the method used to drop the collection.

## Helpful links
- [MongoDB Documentation - drop()](https://docs.mongodb.com/manual/reference/method/db.collection.drop/)

onelinerhub: [How to clear a collection in MongoDB?](https://onelinerhub.com/mongodb/how-to-clear-a-collection-in-mongodb)