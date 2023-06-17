# How to use the NOT IN operator in PostgreSQL?
// plain

The NOT IN operator in PostgreSQL is used to test if a value is not present in a list of values. This operator is used in the WHERE clause of a SELECT, UPDATE, or DELETE statement.

For example, if you want to select all customers who are not in the list of specified cities, you could use the following code:

```
SELECT *
FROM customers
WHERE city NOT IN ('New York', 'Los Angeles', 'Chicago');
```

This statement will return all customers who are not from the cities of New York, Los Angeles, or Chicago.

The parts of the code are:

* `SELECT *` - This statement is used to select all columns from the customers table.
* `FROM customers` - This statement specifies the table from which to select the data.
* `WHERE city NOT IN ('New York', 'Los Angeles', 'Chicago')` - This statement is used to filter out all customers who are not from the specified cities.

## Helpful links

* [PostgreSQL Documentation](https://www.postgresql.org/docs/current/sql-select.html)
* [W3Schools PostgreSQL Tutorial](https://www.w3schools.com/sql/sql_syntax.asp)

onelinerhub: [How to use the NOT IN operator in PostgreSQL?](https://onelinerhub.com/postgresql/how-to-use-the-not-in-operator-in-postgresql)