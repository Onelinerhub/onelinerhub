# How do I use variables in a SQLite database?
// plain

Variables can be used in SQLite databases by using the `PRAGMA` command. This command allows you to set and retrieve variables within the database.

For example, to set the `temp_store` variable to `MEMORY`:
```
PRAGMA temp_store = MEMORY;
```

To retrieve the current value of the `temp_store` variable:
```
PRAGMA temp_store;
```

## Output example

```
temp_store=MEMORY
```

The `PRAGMA` command can also be used to set and retrieve other variables such as `synchronous`, `foreign_keys`, `journal_mode`, and `cache_size`.

## Code explanation

1. `PRAGMA` command - used to set and retrieve variables within the database
2. `temp_store` - variable used to set the store mode for temporary tables
3. `MEMORY` - store mode for temporary tables

## Helpful links
1. https://www.sqlite.org/pragma.html
2. https://www.techonthenet.com/sqlite/pragma.php

onelinerhub: [How do I use variables in a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-use-variables-in-a-sqlite-database)