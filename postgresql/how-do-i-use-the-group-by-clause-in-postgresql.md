# How do I use the GROUP BY clause in PostgreSQL?
// plain

The `GROUP BY` clause is used in PostgreSQL to group together rows of data from a table that have the same values in one or more columns. It is typically used in conjunction with the `SELECT` and `HAVING` clauses.

For example, to group together all the rows in the `orders` table that have the same `customer_id` and get the total number of orders for each customer, the following query could be used:

```
SELECT customer_id, COUNT(*)
FROM orders
GROUP BY customer_id;
```

The output of this query would be:

```
 customer_id | count
-------------+-------
          10 |     3
          11 |     2
          12 |     5
(3 rows)
```

The components of this query are:

* `SELECT`: This clause is used to specify the columns that will be included in the output. In this case, the `customer_id` and the `count` of orders for each customer.
* `FROM`: This clause is used to specify the table that will be used in the query. In this case, the `orders` table.
* `GROUP BY`: This clause is used to group together all the rows in the table that have the same values in the specified column(s). In this case, the `customer_id` column.
* `COUNT`: This is an aggregate function used to count the number of rows in each group.

For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-select.html#SQL-GROUPBY).

onelinerhub: [How do I use the GROUP BY clause in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-use-the-group-by-clause-in-postgresql)