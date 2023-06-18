# How do I use UUIDs in SQLite?
// plain

UUIDs (Universally Unique Identifiers) can be used in SQLite to create a unique identifier for each row in a table. To use UUIDs in SQLite, you first need to create a table with a column to store the UUIDs. The following example creates a table named `users` with a column named `uid` to store the UUIDs:

```sql
CREATE TABLE users (
  uid UUID PRIMARY KEY,
  name TEXT
);
```

Then you can insert UUIDs into the table using the `uuid()` function. The following example inserts a row with a new UUID into the `users` table:

```sql
INSERT INTO users (uid, name) VALUES (uuid(), 'John Doe');
```

The `uuid()` function generates a version 4 UUID, which is composed of random numbers and letters.

## Code explanation

* `CREATE TABLE` - creates a table with the specified columns and data types
* `UUID` - the data type used to store the UUIDs
* `PRIMARY KEY` - ensures that each row has a unique identifier
* `INSERT INTO` - inserts a row into the specified table
* `uuid()` - generates a new version 4 UUID

## Helpful links
* [UUIDs in SQLite](https://www.sqlite.org/uuid.html)
* [SQLite Data Types](https://www.sqlite.org/datatype3.html)

onelinerhub: [How do I use UUIDs in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-uuids-in-sqlite)