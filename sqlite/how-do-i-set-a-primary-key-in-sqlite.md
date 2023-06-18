# How do I set a primary key in SQLite?
// plain

Setting a primary key in SQLite is an important step when creating a new table. A primary key is a column or set of columns that uniquely identifies each row in the table.

To set a primary key in SQLite, use the following syntax:

```
CREATE TABLE <table_name> (
    <column_name1> <data_type>,
    <column_name2> <data_type>,
    <column_name3> <data_type>,
    PRIMARY KEY (<column_name1>, <column_name2>)
);
```

This will create a table with three columns, `column_name1`, `column_name2`, and `column_name3` and set a primary key on the combination of `column_name1` and `column_name2`.

If you need to set a primary key on a single column, you can use the following syntax:

```
CREATE TABLE <table_name> (
    <column_name1> <data_type> PRIMARY KEY
);
```

This will create a table with a single column, `column_name1`, and set it as the primary key.

## Helpful links

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Primary Key](https://www.sqlitetutorial.net/sqlite-primary-key/)

onelinerhub: [How do I set a primary key in SQLite?](https://onelinerhub.com/sqlite/how-do-i-set-a-primary-key-in-sqlite)