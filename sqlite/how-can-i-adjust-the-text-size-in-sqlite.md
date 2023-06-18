# How can I adjust the text size in SQLite?
// plain

To adjust the text size in SQLite, you can use the `PRAGMA` command. The `PRAGMA` command allows you to adjust several settings related to the database. To adjust the text size, you can use the `PRAGMA` command with the `page_size` option.

For example, the following code sets the text size to `4096` bytes:
```
PRAGMA page_size=4096;
```

## Code explanation

- `PRAGMA`: the command used to adjust SQLite settings.
- `page_size`: the option used to adjust the text size.
- `4096`: the size of the text in bytes.

## Helpful links
- [SQLite Documentation](https://www.sqlite.org/pragma.html#pragma_page_size)

onelinerhub: [How can I adjust the text size in SQLite?](https://onelinerhub.com/sqlite/how-can-i-adjust-the-text-size-in-sqlite)