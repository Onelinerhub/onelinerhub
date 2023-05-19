# How to use the "and" operator in MongoDB?
// plain

The `and` operator in MongoDB is used to combine two or more expressions and retrieve documents that match all the expressions in the query.

For example, the following query will return documents that have the `name` field set to `John` and the `age` field set to `25`:

```
db.collection.find({name: "John", age: 25})
```

The output of the above query will be documents that match both the `name` and `age` criteria:

```
{
  "_id": ObjectId("5f3d7f3f3f3f3f3f3f3f3f3f"),
  "name": "John",
  "age": 25
}
```

The `and` operator can also be used to combine multiple expressions in a single query. For example, the following query will return documents that have the `name` field set to `John`, the `age` field set to `25` and the `gender` field set to `male`:

```
db.collection.find({name: "John", age: 25, gender: "male"})
```

The output of the above query will be documents that match all the criteria:

```
{
  "_id": ObjectId("5f3d7f3f3f3f3f3f3f3f3f3f"),
  "name": "John",
  "age": 25,
  "gender": "male"
}
```

The `and` operator can also be used to combine multiple expressions in a single query using the `$and` operator. For example, the following query will return documents that have the `name` field set to `John` and the `age` field set to `25` or the `gender` field set to `male`:

```
db.collection.find({$and: [{name: "John"}, {$or: [{age: 25}, {gender: "male"}]}]})
```

The output of the above query will be documents that match either the `name` and `age` criteria or the `name` and `gender` criteria:

```
{
  "_id": ObjectId("5f3d7f3f3f3f3f3f3f3f3f3f"),
  "name": "John",
  "age": 25
},
{
  "_id": ObjectId("5f3d7f3f3f3f3f3f3f3f3f3f"),
  "name": "John",
  "gender": "male"
}
```

## Helpful links

- [MongoDB Documentation - Logical Query Operators](https://docs.mongodb.com/manual/reference/operator/query-logical/)

onelinerhub: [How to use the "and" operator in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-the--and--operator-in-mongodb)