# How do I use an enum data type with SQLite?
// plain

Enums are data types that allow you to define a list of valid values for a given column in a SQLite database. To use an enum data type in SQLite, you need to use the `CREATE TABLE` statement to create a table with the desired column. The syntax for creating a column with an enum data type is as follows:

```
CREATE TABLE table_name (
  column_name ENUM('value1', 'value2', 'value3', ...)
);
```

For example, if you wanted to create a table with a column that only accepts values of 'yes' or 'no', you could do the following:

```
CREATE TABLE responses (
  answer ENUM('yes', 'no')
);
```

Once the table is created, you can use the `INSERT` statement to add data to the table. The syntax for the `INSERT` statement is as follows:

```
INSERT INTO table_name (column_name)
VALUES ('value');
```

For example, if you wanted to insert a 'yes' value into the `responses` table, you could do the following:

```
INSERT INTO responses (answer)
VALUES ('yes');
```

You can also use the `SELECT` statement to query data from the table. The syntax for the `SELECT` statement is as follows:

```
SELECT column_name
FROM table_name;
```

For example, if you wanted to get all the values from the `responses` table, you could do the following:

```
SELECT answer
FROM responses;
```

This would return all the values from the `responses` table, which in this case would be 'yes' and 'no'.

## Helpful links

- [SQLite Documentation: Data Types](https://www.sqlite.org/datatype3.html#enum)
- [SQLite Documentation: CREATE TABLE](https://www.sqlite.org/lang_createtable.html)

onelinerhub: [How do I use an enum data type with SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-an-enum-data-type-with-sqlite)