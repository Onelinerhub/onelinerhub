# How do I use an array in SQLite?
// plain

An array is a data structure that allows for the storage of multiple values in one variable. In SQLite, this is accomplished by using the CREATE TABLE statement.

Here is an example of how to create a table with an array field in SQLite:
```
CREATE TABLE myTable (
  id INTEGER PRIMARY KEY,
  array_field TEXT ARRAY
);
```

This example creates a table called "myTable" with an array field called "array_field".

To insert values into the array field, use the INSERT statement. Here is an example:
```
INSERT INTO myTable (array_field)
  VALUES (ARRAY [1, 2, 3]);
```

This example inserts the values 1, 2, and 3 into the array field.

To retrieve the values from the array field, use the SELECT statement. Here is an example:
```
SELECT array_field FROM myTable;
```

This example retrieves the values from the array field.

## Helpful links
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Arrays](https://www.sqlitetutorial.net/sqlite-arrays/)

onelinerhub: [How do I use an array in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-an-array-in-sqlite)