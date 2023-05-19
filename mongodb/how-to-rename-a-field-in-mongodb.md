# How to rename a field in MongoDB?
// plain

Renaming a field in MongoDB can be done using the `$rename` operator. This operator takes two parameters, the first being the name of the field to be renamed and the second being the new name of the field.

For example, to rename the field `name` to `fullName` in the collection `users`, the following command can be used:
```
db.users.updateMany({}, {$rename: {name: "fullName"}})
```

The code above will update all documents in the `users` collection, renaming the `name` field to `fullName`.

## Code explanation


1. `db.users.updateMany({}, {$rename: {name: "fullName"}})` - This is the command used to update all documents in the `users` collection, renaming the `name` field to `fullName`.

2. `$rename` - This is the operator used to rename a field in MongoDB.

3. `name` - This is the name of the field to be renamed.

4. `fullName` - This is the new name of the field.

## Helpful links

- [MongoDB Documentation - $rename](https://docs.mongodb.com/manual/reference/operator/update/rename/)

onelinerhub: [How to rename a field in MongoDB?](https://onelinerhub.com/mongodb/how-to-rename-a-field-in-mongodb)