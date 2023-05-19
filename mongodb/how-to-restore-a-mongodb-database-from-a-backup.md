# How to restore a MongoDB database from a backup?
// plain

Restoring a MongoDB database from a backup is a simple process.

1. Create a directory to store the backup files.
2. Use the `mongorestore` command to restore the database from the backup files.
   ```
   mongorestore --db <database_name> <backup_directory>
   ```
3. The `--db` option specifies the name of the database to restore.
4. The `<backup_directory>` argument is the directory containing the backup files.
5. For more information, please refer to the [MongoDB documentation](https://docs.mongodb.com/manual/reference/program/mongorestore/).

onelinerhub: [How to restore a MongoDB database from a backup?](https://onelinerhub.com/mongodb/how-to-restore-a-mongodb-database-from-a-backup)