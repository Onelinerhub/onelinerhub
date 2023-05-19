# How to use transactions in MongoDB?
// plain

MongoDB transactions provide atomicity, consistency, isolation, and durability (ACID) guarantees for operations within a single document. Transactions allow developers to execute multiple operations in a single atomic operation, either all of the operations will succeed or none of them will.

## Example code

```
// Start a session
const session = db.startSession();

// Start a transaction
session.startTransaction();

// Insert a document
db.collection.insertOne({
  _id: 1,
  name: 'John Doe'
}, { session });

// Update a document
db.collection.updateOne({
  _id: 1
}, {
  $set: {
    name: 'Jane Doe'
  }
}, { session });

// Commit the transaction
session.commitTransaction();

// End the session
session.endSession();
```

## Output example

```
WriteResult({ "nInserted" : 1 })
```

## Code explanation


1. `const session = db.startSession();` - This line starts a session.

2. `session.startTransaction();` - This line starts a transaction.

3. `db.collection.insertOne({ _id: 1, name: 'John Doe' }, { session });` - This line inserts a document with the given data.

4. `db.collection.updateOne({ _id: 1 }, { $set: { name: 'Jane Doe' } }, { session });` - This line updates the document with the given data.

5. `session.commitTransaction();` - This line commits the transaction.

6. `session.endSession();` - This line ends the session.

## Helpful links

- [MongoDB Transactions](https://docs.mongodb.com/manual/core/transactions/)
- [MongoDB Node.js Driver Transactions](https://mongodb.github.io/node-mongodb-native/3.3/tutorials/transactions/)

onelinerhub: [How to use transactions in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-transactions-in-mongodb)