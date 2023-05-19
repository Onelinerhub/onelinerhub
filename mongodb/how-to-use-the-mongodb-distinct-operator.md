# How to use the MongoDB distinct operator?
// plain

The MongoDB `distinct` operator is used to find the distinct values for a specified field across a single collection. It returns an array of the distinct values.

## Example

```
db.collection.distinct("field")
```

## Output example

```
[value1, value2, value3, ...]
```

## Code explanation

- `db.collection`: specifies the collection from which to retrieve the distinct values
- `distinct("field")`: specifies the field for which to return distinct values

## Helpful links
- [MongoDB Documentation - distinct](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/)

onelinerhub: [How to use the MongoDB distinct operator?](https://onelinerhub.com/mongodb/how-to-use-the-mongodb-distinct-operator)