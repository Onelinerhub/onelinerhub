# How do I use Amazon Redshift RSQL to query data?
// plain

Amazon Redshift RSQL is a powerful, fully managed, petabyte-scale data warehouse service. It allows you to quickly and easily query data in the cloud. You can use RSQL to query data stored in Amazon Redshift using the SQL-like language.

Here is an example of a query to retrieve all rows from a table called 'Customers':

```
SELECT *
FROM Customers;
```

This query will return all columns and rows from the 'Customers' table.

The query can also be used to filter the data, for example to return only customers from the state of California:

```
SELECT *
FROM Customers
WHERE state = 'CA';
```

This query will return all columns and rows from the 'Customers' table where the `state` column has a value of `CA`.

You can also use RSQL to join multiple tables together, for example to join the 'Customers' table with the 'Orders' table:

```
SELECT c.name, o.order_total
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id;
```

This query will return the `name` column from the 'Customers' table and the `order_total` column from the 'Orders' table, where the `customer_id` from both tables match.

For more information on using Amazon Redshift RSQL, please refer to the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_SQL_commands.html).

onelinerhub: [How do I use Amazon Redshift RSQL to query data?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-rsql-to-query-data)