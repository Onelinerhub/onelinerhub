# How to convert MongoDB ObjectId to string?
// plain

MongoDB ObjectId is a 12-byte BSON type used as a unique identifier for documents within a collection. It can be converted to a string using the `toString()` method.

## Example code

```
const ObjectId = require('mongodb').ObjectId;
const id = new ObjectId();
const stringId = id.toString();
console.log(stringId);
```

## Output example

```
5f3f9f9f9f9f9f9f9f9f9f9
```

## Code explanation

- `const ObjectId = require('mongodb').ObjectId;`: This line imports the ObjectId class from the mongodb package.
- `const id = new ObjectId();`: This line creates a new ObjectId instance.
- `const stringId = id.toString();`: This line converts the ObjectId instance to a string.
- `console.log(stringId);`: This line prints the string to the console.

## Helpful links
- [MongoDB ObjectId](https://docs.mongodb.com/manual/reference/method/ObjectId/)

onelinerhub: [How to convert MongoDB ObjectId to string?](https://onelinerhub.com/mongodb/how-to-convert-mongodb-objectid-to-string)