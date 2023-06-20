# How do I use Google BigQuery language to query data?
// plain

Google BigQuery is a serverless, highly scalable, and cost-effective cloud data warehouse. It enables you to query large datasets using a SQL-like language called BigQuery SQL. Here is an example of a query in BigQuery SQL to count the number of records in a table:

```
SELECT COUNT(*)
FROM `bigquery-public-data.samples.shakespeare`
```

## Output example

```
COUNT(*)
112376
```

## Code explanation


* `SELECT` - specifies which columns of the table you want to query. In this case, the asterisk (*) is used to select all columns.
* `FROM` - specifies the source table you want to query. In this case, the table is `bigquery-public-data.samples.shakespeare`.
* `COUNT(*)` - returns the number of records that meet the criteria of the `SELECT` statement.

For more information on using BigQuery SQL to query data, please refer to the [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/).

onelinerhub: [How do I use Google BigQuery language to query data?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-language-to-query-data)