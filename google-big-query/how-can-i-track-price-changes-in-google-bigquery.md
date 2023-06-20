# How can I track price changes in Google BigQuery?
// plain

The following example demonstrates how to track price changes in Google BigQuery.

```
SELECT
  product_id,
  price,
  TIMESTAMP_DIFF(price_change_date, LAG(price_change_date, 1) OVER (PARTITION BY product_id ORDER BY price_change_date), SECOND) as price_change_interval
FROM
  `project.dataset.table`
```

This query will return the product ID, price, and the interval between price changes for each product. The `TIMESTAMP_DIFF` function is used to calculate the interval between two timestamps. The `LAG` window function is used to access the previous row's price change date.

The output of this query would look something like this:
```
product_id  price  price_change_interval
1           10.99  NULL
1           11.99  86400
1           12.99  86400
2           9.99   NULL
2           10.99  86400
```

The parts of this query are as follows:

* `SELECT`: specifies the columns to be returned by the query
* `TIMESTAMP_DIFF`: calculates the difference between two timestamps
* `LAG`: window function that returns the value of a column from the previous row
* `PARTITION BY`: specifies the column used to divide the data into partitions
* `ORDER BY`: specifies the column used to order the data within each partition

## Helpful links
* [BigQuery SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/)
* [BigQuery Window Functions](https://cloud.google.com/bigquery/docs/reference/standard-sql/window_functions)

onelinerhub: [How can I track price changes in Google BigQuery?](https://onelinerhub.com/google-big-query/how-can-i-track-price-changes-in-google-bigquery)