# How do I use SQLite UNION to combine multiple SELECT queries?
// plain

SQLite UNION is a keyword used to combine the results of two or more SELECT queries into a single result set. It is helpful for combining data from multiple tables or from multiple queries into a single result.

## Example

```
SELECT name, age
FROM table1
UNION
SELECT name, age
FROM table2;
```

## Output example

```
name      age
--------  ----
John      25
Mary      28
James     32
```

- `SELECT name, age`: Retrieve the `name` and `age` columns from the respective tables.
- `FROM table1`: Retrieve data from table1.
- `UNION`: Combine the results of the two SELECT queries into a single result set.
- `FROM table2`: Retrieve data from table2.

## Helpful links
- [SQLite UNION](https://www.sqlitetutorial.net/sqlite-union/)
- [SQLite UNION ALL](https://www.sqlitetutorial.net/sqlite-union-all/)

onelinerhub: [How do I use SQLite UNION to combine multiple SELECT queries?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-union-to-combine-multiple-select-queries)