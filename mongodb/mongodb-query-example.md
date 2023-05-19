# MongoDB query example
// plain

MongoDB is a document-oriented NoSQL database used for high volume data storage. It is an open-source database that uses a document-oriented data model, which means data is stored in JSON-like documents with dynamic schemas.

Below is an example of a MongoDB query that finds all documents in the collection "users" where the "age" field is greater than or equal to 18:

```
db.users.find({ age: { $gte: 18 } })
```

The output of this query would be a list of documents in the "users" collection where the "age" field is greater than or equal to 18.

## Code explanation


- `db.users`: This is the collection that the query is searching in.
- `find()`: This is the method used to search the collection.
- `{ age: { $gte: 18 } }`: This is the query condition, which specifies that the documents returned must have an "age" field greater than or equal to 18.

## Helpful links

- [MongoDB Documentation](https://docs.mongodb.com/)
- [MongoDB Query Tutorial](https://www.tutorialspoint.com/mongodb/mongodb_query_document.htm)

onelinerhub: [MongoDB query example](https://onelinerhub.com/mongodb/mongodb-query-example)