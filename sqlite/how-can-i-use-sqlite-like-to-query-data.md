# How can I use SQLite LIKE to query data?
// plain

The SQLite LIKE operator is used to query data based on a pattern. It is used to search for specific strings of characters in a column of a database table. It is similar to the '%' wildcard operator used in other databases.

For example, to search for all rows in a table that contain the string 'SQLite' in the 'name' column, the following statement can be used:

```
SELECT * FROM table_name WHERE name LIKE '%SQLite%';
```

The output of this query will be all rows in the table that have the string 'SQLite' in the 'name' column.

The LIKE operator can also be used with the underscore character '_' to represent any single character. For example, to search for all rows in a table that contain the string 'SQL_te' in the 'name' column, the following statement can be used:

```
SELECT * FROM table_name WHERE name LIKE 'SQL_te';
```

The output of this query will be all rows in the table that have the string 'SQL_te' in the 'name' column.

The LIKE operator can also be used with the '[]' character to represent any single character within the range specified. For example, to search for all rows in a table that contain the string 'SQL[aeiou]te' in the 'name' column, the following statement can be used:

```
SELECT * FROM table_name WHERE name LIKE 'SQL[aeiou]te';
```

The output of this query will be all rows in the table that have the string 'SQL[aeiou]te' in the 'name' column.

## Helpful links
- SQLite Documentation: https://www.sqlite.org/docs.html
- SQLite LIKE Operator: https://www.sqlitetutorial.net/sqlite-like/

onelinerhub: [How can I use SQLite LIKE to query data?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-like-to-query-data)