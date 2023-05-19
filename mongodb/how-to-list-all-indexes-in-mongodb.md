# How to list all indexes in MongoDB?
// plain

To list all indexes in MongoDB, you can use the `db.collection.getIndexes()` command. This command will return an array of documents that contain information about all the indexes in the specified collection.

## Example code

```
db.collection.getIndexes()
```

Example output:
```
[
  {
    "v" : 2,
    "key" : {
      "_id" : 1
    },
    "name" : "_id_",
    "ns" : "test.collection"
  },
  {
    "v" : 2,
    "key" : {
      "name" : 1
    },
    "name" : "name_1",
    "ns" : "test.collection"
  }
]
```

## Code explanation

- `db.collection.getIndexes()`: This command will return an array of documents that contain information about all the indexes in the specified collection.
- `v`: This is the version of the index.
- `key`: This is the key pattern of the index.
- `name`: This is the name of the index.
- `ns`: This is the namespace of the index.

## Helpful links
- [MongoDB Documentation - db.collection.getIndexes()](https://docs.mongodb.com/manual/reference/method/db.collection.getIndexes/)

onelinerhub: [How to list all indexes in MongoDB?](https://onelinerhub.com/mongodb/how-to-list-all-indexes-in-mongodb)