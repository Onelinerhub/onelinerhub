# How can I use Sphinx Search to group my data?
// plain

Sphinx Search can be used to group data by using the GROUP BY clause. This clause allows you to group your data by one or more columns, and then aggregate the results.

For example, to group a table of customer orders by their order status, you can use the following query:

```
SELECT order_status, COUNT(*) FROM orders GROUP BY order_status;
```

This query will return the number of orders with each order status.

The parts of the query are:
- `SELECT order_status, COUNT(*)` - This part of the query specifies the columns to be returned. In this case, it is the order status and the number of orders with that status.
- `FROM orders` - This part of the query specifies the table from which the data should be retrieved.
- `GROUP BY order_status` - This part of the query specifies the column by which the data should be grouped.

The output of the query will look something like this:

```
order_status  COUNT(*)
pending       5
shipped       10
cancelled     3
```

For more information about using Sphinx Search to group data, see [this page](https://sphinxsearch.com/docs/current.html#group-by).

onelinerhub: [How can I use Sphinx Search to group my data?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-to-group-my-data)