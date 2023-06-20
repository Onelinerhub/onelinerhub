# How can I use Google BigQuery to create a pivot table?
// plain

Google BigQuery is a powerful data warehouse tool that can be used to create a pivot table. A pivot table is a type of summary table that allows users to quickly summarize large datasets.

To create a pivot table in BigQuery, you must first create a query that contains the data you want to summarize. For example, the following query will return the total number of orders for each product in the orders table:

```sql
SELECT product, COUNT(*) AS num_orders
FROM orders
GROUP BY product
```

## Output example


```
product	num_orders
Product A	100
Product B	200
Product C	300
```

Once the query is written, you can use the `pivot` clause to create the pivot table. The following example will create a pivot table that displays the total number of orders for each product by month:

```sql
SELECT *
FROM (
  SELECT product, EXTRACT(MONTH FROM order_date) AS month, COUNT(*) AS num_orders
  FROM orders
  GROUP BY product, month
)
PIVOT (
  SUM(num_orders)
  FOR month IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
)
```

## Output example


```
product	1	2	3	4	5	6	7	8	9	10	11	12
Product A	10	20	30	40	50	60	70	80	90	100	110	120
Product B	20	40	60	80	100	120	140	160	180	200	220	240
Product C	30	60	90	120	150	180	210	240	270	300	330	360
```

The code above consists of two parts:

1. The inner query `SELECT product, EXTRACT(MONTH FROM order_date) AS month, COUNT(*) AS num_orders FROM orders GROUP BY product, month` which returns the total number of orders for each product by month.

2. The `PIVOT` clause which creates the pivot table from the query results, using the `SUM` aggregation function to calculate the total number of orders for each product by month.

For more information about creating pivot tables in BigQuery, please refer to the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#pivot-clause).

onelinerhub: [How can I use Google BigQuery to create a pivot table?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-create-a-pivot-table)