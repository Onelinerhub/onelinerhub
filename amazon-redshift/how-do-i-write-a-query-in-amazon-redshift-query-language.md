# How do I write a query in Amazon Redshift query language?
// plain

A query in Amazon Redshift query language (SQL) is a command used to retrieve data from a database. The query consists of a SELECT statement, which indicates the columns and/or expressions to be returned, and a FROM clause which indicates the tables and/or views to be queried.

For example, the following query will return the total number of orders placed by each customer in the database:

```sql
SELECT customer_id, COUNT(*) AS orders_placed
FROM orders
GROUP BY customer_id;
```

The query consists of the following parts:

* `SELECT` - indicates the columns to be returned in the query results. In this example, the `customer_id` and the result of the expression `COUNT(*)` are specified.
* `FROM` - indicates the tables and/or views to be queried. In this example, the `orders` table is specified.
* `GROUP BY` - groups the results of the query by the specified columns. In this example, the results are grouped by `customer_id`.

The output of this query would look something like this:

```
 customer_id | orders_placed
------------+---------------
         10 |             5
         11 |             3
         12 |             8
```

For more information on Amazon Redshift query language, see the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_SQL_commands.html).

onelinerhub: [How do I write a query in Amazon Redshift query language?](https://onelinerhub.com/amazon-redshift/how-do-i-write-a-query-in-amazon-redshift-query-language)