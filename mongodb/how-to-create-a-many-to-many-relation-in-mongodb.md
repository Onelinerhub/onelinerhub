# How to create a many to many relation in MongoDB?
// plain

MongoDB supports many-to-many relationships through the use of embedded documents and document references. To create a many-to-many relationship in MongoDB, we need to create two collections, one for each entity in the relationship. For example, if we have a `users` collection and a `groups` collection, we can create a many-to-many relationship between them by embedding a `groups` array in each `user` document and a `users` array in each `group` document.

## Example code

```
// Create users collection
db.createCollection("users")

// Create groups collection
db.createCollection("groups")

// Insert a user
db.users.insert({
  name: "John Doe",
  groups: []
})

// Insert a group
db.groups.insert({
  name: "Group A",
  users: []
})

// Add user to group
db.groups.update(
  { name: "Group A" },
  { $push: { users: { $ref: "users", $id: ObjectId("5f3f9f9f9f9f9f9f9f9f9f9f") } } }
)

// Add group to user
db.users.update(
  { name: "John Doe" },
  { $push: { groups: { $ref: "groups", $id: ObjectId("5f3f9f9f9f9f9f9f9f9f9f9f") } } }
)
```

## Output example

```
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

## Code explanation


- `db.createCollection("users")`: This creates a collection called `users` in the current database.

- `db.users.insert({ name: "John Doe", groups: [] })`: This inserts a document into the `users` collection with the name `John Doe` and an empty `groups` array.

- `db.groups.insert({ name: "Group A", users: [] })`: This inserts a document into the `groups` collection with the name `Group A` and an empty `users` array.

- `db.groups.update({ name: "Group A" }, { $push: { users: { $ref: "users", $id: ObjectId("5f3f9f9f9f9f9f9f9f9f9f9f") } } })`: This updates the `groups` collection by pushing a reference to the `users` collection with the `_id` of the user document to the `users` array in the `Group A` document.

- `db.users.update({ name: "John Doe" }, { $push: { groups: { $ref: "groups", $id: ObjectId("5f3f9f9f9f9f9f9f9f9f9f9f") } } })`: This updates the `users` collection by pushing a reference to the `groups` collection with the `_id` of the group document to the `groups` array in the `John Doe` document.

## Helpful links

- [MongoDB Documentation - Relationships](https://docs.mongodb.com/manual/tutorial/model-referenced-one-to-many-relationships-between-documents/)

onelinerhub: [How to create a many to many relation in MongoDB?](https://onelinerhub.com/mongodb/how-to-create-a-many-to-many-relation-in-mongodb)