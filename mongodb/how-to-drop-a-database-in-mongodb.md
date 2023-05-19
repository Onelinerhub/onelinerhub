# How to drop a database in MongoDB?
// plain

To drop a database in MongoDB, use the `dropDatabase()` method. This method will delete the current database.

## Example

```
use myDatabase
db.dropDatabase()
```
## Output example

```
{ "dropped" : "myDatabase", "ok" : 1 }
```

The `dropDatabase()` method takes no arguments and returns a document with the field `dropped` containing the name of the database that was dropped.

## Code explanation

- `use myDatabase`: This command is used to switch to the database that you want to drop.
- `db.dropDatabase()`: This command is used to drop the current database.

## Helpful links
- [MongoDB Documentation - dropDatabase](https://docs.mongodb.com/manual/reference/method/db.dropDatabase/)

onelinerhub: [How to drop a database in MongoDB?](https://onelinerhub.com/mongodb/how-to-drop-a-database-in-mongodb)