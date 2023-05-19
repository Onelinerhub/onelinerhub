# How to backup a MongoDB database?
// plain

Backup of a MongoDB database can be done using the `mongodump` command. This command will create a binary dump of the contents of the database.

## Example

```
mongodump --db mydb --out /data/backup/
```

This command will create a backup of the `mydb` database in the `/data/backup/` directory.

The `mongodump` command has several options that can be used to customize the backup process. These include:

- `--db`: Specify the database to backup
- `--collection`: Specify the collection to backup
- `--out`: Specify the output directory
- `--query`: Specify a query to filter the documents to backup

For more information, please refer to the [MongoDB documentation](https://docs.mongodb.com/manual/reference/program/mongodump/).

onelinerhub: [How to backup a MongoDB database?](https://onelinerhub.com/mongodb/how-to-backup-a-mongodb-database)