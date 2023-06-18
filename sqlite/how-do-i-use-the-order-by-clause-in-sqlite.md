# How do I use the ORDER BY clause in SQLite?
// plain

The ORDER BY clause is used in SQLite to sort the results of a query in ascending or descending order.

## Example

```
SELECT * FROM customers ORDER BY last_name ASC;
```

This query will return the rows in the customers table sorted by the last_name column in ascending order.

## Code explanation

- SELECT: This is the keyword used to select data from a database.
- *: This is a wildcard character that will select all columns from the table.
- FROM: This is the keyword used to specify the table from which data will be selected.
- ORDER BY: This is the keyword used to sort the results of a query.
- last_name: This is the name of the column by which the results will be sorted.
- ASC: This is the keyword used to specify that the results should be sorted in ascending order.

## Helpful links
- https://www.sqlitetutorial.net/sqlite-order-by/
- https://www.sqlitetutorial.net/sqlite-select/

onelinerhub: [How do I use the ORDER BY clause in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-the-order-by-clause-in-sqlite)