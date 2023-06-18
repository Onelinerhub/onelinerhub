# How do I use query parameters with SQLite?
// plain

Query parameters with SQLite can be used to filter, sort, and update data stored in a SQLite database.

For example, to filter a table for all records where the `name` column equals 'John', the following query can be used:

```
SELECT * FROM table_name WHERE name = 'John';
```

This query will return all records where the `name` column is equal to 'John'.

To sort the table by the `name` column in descending order, the following query can be used:

```
SELECT * FROM table_name ORDER BY name DESC;
```

This query will return all records sorted by the `name` column in descending order.

To update a record in the table, the following query can be used:

```
UPDATE table_name SET name = 'John' WHERE id = 1;
```

This query will update the record with the `id` equal to 1, setting the `name` column to 'John'.

## Helpful links
- [SQLite Query Language](https://www.sqlite.org/lang.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How do I use query parameters with SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-query-parameters-with-sqlite)