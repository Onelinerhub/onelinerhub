# How do I get the column names of a SQLite database?
// plain

To get the column names of a SQLite database, you can use the `PRAGMA table_info` statement. This statement returns the column names, data types, and other information about the columns in a given table.

For example, to get the column names of a table called `people`:

```
sqlite> PRAGMA table_info(people);
0|name|text|1||0
1|age|integer|0||0
2|gender|text|0||0
```

The output of the `PRAGMA table_info` statement consists of the following parts:

- `0`: The column number
- `name`: The column name
- `text`: The data type of the column
- `1`: A flag indicating whether the column is `NOT NULL`
- `0`: A flag indicating whether the column is a `PRIMARY KEY`
- `0`: A flag indicating whether the column has a `DEFAULT VALUE`

## Helpful links
- [SQLite Documentation - PRAGMA table_info](https://www.sqlite.org/pragma.html#pragma_table_info)

onelinerhub: [How do I get the column names of a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-get-the-column-names-of-a-sqlite-database)