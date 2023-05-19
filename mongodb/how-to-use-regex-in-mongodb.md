# How to use regex in MongoDB?
// plain

MongoDB supports the use of regular expressions to search for strings within documents. To use regex in MongoDB, the `$regex` operator is used in a `find()` query.

For example, the following query will find all documents in the `users` collection where the `name` field contains the string `John`:

```
db.users.find({name: {$regex: /John/}})
```

The code above consists of the following parts:

- `db.users.find()`: This is the `find()` query used to search for documents in the `users` collection.
- `{name: {$regex: /John/}}`: This is the condition used to search for documents where the `name` field contains the string `John`. The `$regex` operator is used to specify that a regular expression should be used for the search. The regular expression `/John/` is used to search for the string `John`.

For more information, see the [MongoDB documentation](https://docs.mongodb.com/manual/reference/operator/query/regex/).

onelinerhub: [How to use regex in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-regex-in-mongodb)