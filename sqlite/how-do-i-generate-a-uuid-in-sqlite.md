# How do I generate a UUID in SQLite?
// plain

To generate a UUID in SQLite, use the `sqlite3_create_function` function to register a UUID generating function. The following example code will create a new UUID and store it in the `uuid` variable:

```
sqlite3 *db;
sqlite3_create_function(db, "uuid", 0, SQLITE_ANY, 0, uuid_generate, 0, 0);
char *uuid;
sqlite3_exec(db, "SELECT uuid()", uuid_callback, &uuid, 0);
```

The `uuid_generate` function is a custom function that generates a UUID and the `uuid_callback` function is a callback function that stores the generated UUID in the `uuid` variable.

For more information on UUIDs in SQLite, see the [SQLite documentation](https://www.sqlite.org/lang_corefunc.html#uuid).

onelinerhub: [How do I generate a UUID in SQLite?](https://onelinerhub.com/sqlite/how-do-i-generate-a-uuid-in-sqlite)