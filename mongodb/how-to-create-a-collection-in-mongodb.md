# How to create a collection in MongoDB?
// plain

Creating a collection in MongoDB is a simple process. To create a collection, use the `db.createCollection()` method. The syntax for this method is as follows:
```
db.createCollection(name, options)
```

- `name`: The name of the collection to be created.
- `options`: This is an optional parameter. It is a document that specifies the configuration of the collection.

## Example

```
db.createCollection("customers", { capped : true, autoIndexId : true, size : 6142800, max : 10000 } )
```
## Output example

```
{ "ok" : 1 }
```

## Helpful links
- [MongoDB Documentation - createCollection](https://docs.mongodb.com/manual/reference/method/db.createCollection/)

onelinerhub: [How to create a collection in MongoDB?](https://onelinerhub.com/mongodb/how-to-create-a-collection-in-mongodb)