# How to use MongoDB HTTP interface?
// plain

MongoDB provides an HTTP interface for interacting with the database. It can be used to perform CRUD operations, run queries, and manage indexes.

Example code to insert a document into a collection:
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:28017/mydb/mycollection
```

## Output example

```
{"ok":1}
```

The code consists of the following parts:

- `curl`: the command used to make the HTTP request
- `-X POST`: the type of request, in this case a POST request
- `-H "Content-Type: application/json"`: the header specifying the content type of the request body
- `-d '{"name": "John Doe"}'`: the data to be sent in the request body
- `http://localhost:28017/mydb/mycollection`: the URL of the MongoDB instance and the collection to which the document should be inserted

## Helpful links

- [MongoDB HTTP Interface Documentation](https://docs.mongodb.com/manual/reference/program/mongod/#http-interfaces)

onelinerhub: [How to use MongoDB HTTP interface?](https://onelinerhub.com/mongodb/how-to-use-mongodb-http-interface)