# sensitive

How do I make SQLite searches case sensitive?
// plain

In order to make SQLite searches case sensitive, you must use the COLLATE NOCASE clause in your SELECT statement. This clause tells SQLite to ignore the case of the strings when comparing them. For example:

```
SELECT * FROM table WHERE name COLLATE NOCASE LIKE '%john%';
```

This query would return all rows that contain the string 'john' in the name field, regardless of the case of the letters.

The COLLATE clause can also be used to compare strings in a case-sensitive manner. For example:

```
SELECT * FROM table WHERE name COLLATE BINARY LIKE '%john%';
```

This query would only return rows that contain 'john' in the name field with the exact same case as the query string.

## Code explanation


1. COLLATE NOCASE: This clause tells SQLite to ignore the case of the strings when comparing them.
2. COLLATE BINARY: This clause tells SQLite to compare strings in a case-sensitive manner.
3. LIKE: This operator is used to compare strings.

## Helpful links

- [SQLite Collation](https://www.sqlite.org/datatype3.html#collation)
- [SQLite LIKE](https://www.sqlite.org/lang_expr.html#likeops)

onelinerhub: [sensitive

How do I make SQLite searches case sensitive?](https://onelinerhub.com/sqlite/sensitive--how-do-i-make-sqlite-searches-case-sensitive)