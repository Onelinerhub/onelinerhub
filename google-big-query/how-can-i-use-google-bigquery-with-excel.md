# How can I use Google BigQuery with Excel?
// plain

You can use Google BigQuery with Excel by using the BigQuery connector for Microsoft Excel. This connector allows you to connect to your BigQuery datasets and run SQL queries directly from Excel.

To use the connector, you will first need to download and install the [Google Cloud Platform plugin for Microsoft Excel](https://cloud.google.com/blog/products/data-analytics/how-to-connect-excel-to-bigquery-and-query-your-data). Once installed, you can use the plugin to connect to your BigQuery dataset and run SQL queries directly from Excel.

For example, to run a query to get the total number of records in a table, you would enter the following code in Excel:

```
SELECT COUNT(*) FROM <table_name>
```

The output of the query will be displayed in Excel:

```
COUNT(*)
100
```

You can also use the plugin to run more complex queries, such as joining tables, filtering data, or aggregating data.

For more information on how to use the BigQuery connector for Microsoft Excel, see the [official documentation](https://cloud.google.com/bigquery/docs/excel-connector).

onelinerhub: [How can I use Google BigQuery with Excel?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-with-excel)