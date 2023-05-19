# How to export an entire MongoDB database?
// plain

To export an entire MongoDB database, you can use the `mongodump` command. This command will create a binary export of the contents of the database.

## Example

```
mongodump --db mydb
```

This will create a dump directory containing the exported data.

The `mongodump` command has several options that can be used to customize the export. These include:

- `--db`: Specify the database to export
- `--collection`: Specify the collection to export
- `--out`: Specify the output directory
- `--query`: Specify a query to filter the documents to export

For more information, see the [MongoDB documentation](https://docs.mongodb.com/manual/reference/program/mongodump/).

onelinerhub: [How to export an entire MongoDB database?](https://onelinerhub.com/mongodb/how-to-export-an-entire-mongodb-database)