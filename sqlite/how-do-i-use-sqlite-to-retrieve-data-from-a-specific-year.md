# How do I use SQLite to retrieve data from a specific year?
// plain

To retrieve data from a specific year using SQLite, you can use the following query:

```
SELECT *
FROM <table_name>
WHERE YEAR(<date_column>) = <year>;
```

This query will return all the records in the table whose date column is in the specified year. For example, if you have a table called `orders` with a column called `order_date` and you wanted to retrieve all the orders from the year 2018, you would use the following query:

```
SELECT *
FROM orders
WHERE YEAR(order_date) = 2018;
```

The parts of the query are:

- `SELECT *` – this specifies that all columns should be returned in the result set.
- `FROM orders` – this specifies that the table to query is called `orders`.
- `WHERE YEAR(order_date) = 2018` – this specifies that only records from the year 2018 should be returned.

## Helpful links

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite YEAR Function](https://www.sqlitetutorial.net/sqlite-date-and-time-functions/sqlite-year-function/)

onelinerhub: [How do I use SQLite to retrieve data from a specific year?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-to-retrieve-data-from-a-specific-year)