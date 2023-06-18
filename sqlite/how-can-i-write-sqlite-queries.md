# How can I write SQLite queries?
// plain

Writing SQLite queries is relatively straightforward. The basic syntax is very similar to other SQL databases like MySQL and PostgreSQL. Here is an example query to select all records from a table called `Customers`:

```
SELECT * FROM Customers;
```

The output of this query will depend on the data in the table, but will generally be a list of all the records in the table.

To narrow down the results, you can use a `WHERE` clause to specify criteria. For example, to select all customers with a `city` of 'New York':

```
SELECT * FROM Customers WHERE city = 'New York';
```

You can also use `ORDER BY` to sort the results, and `LIMIT` to limit the number of rows returned. For example, to select the first 10 customers in alphabetical order:

```
SELECT * FROM Customers ORDER BY name LIMIT 10;
```

You can also use `JOIN` to combine data from multiple tables. For example, to select all customers and their orders:

```
SELECT * FROM Customers
JOIN Orders ON Customers.id = Orders.customer_id;
```

To learn more about writing SQLite queries, you can check out the [SQLite documentation](https://www.sqlite.org/lang.html).

onelinerhub: [How can I write SQLite queries?](https://onelinerhub.com/sqlite/how-can-i-write-sqlite-queries)