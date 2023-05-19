# How to dump a MongoDB database?
// plain

To dump a MongoDB database, you can use the `mongodump` command. This command will create a binary dump of the contents of a MongoDB database.

## Example

```
mongodump --db mydb
```

This will create a dump of the `mydb` database in the current directory.

The `mongodump` command has several options that can be used to customize the dump. For example, you can specify the output directory, the collection to dump, and the query to use when dumping.

Parts of the command:
- `mongodump`: The command to dump a MongoDB database
- `--db`: The option to specify the database to dump
- `mydb`: The name of the database to dump

## Helpful links
- [MongoDB Documentation - mongodump](https://docs.mongodb.com/manual/reference/program/mongodump/)

onelinerhub: [How to dump a MongoDB database?](https://onelinerhub.com/mongodb/how-to-dump-a-mongodb-database)