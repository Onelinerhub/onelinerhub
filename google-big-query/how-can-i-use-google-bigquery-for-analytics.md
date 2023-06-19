# How can I use Google BigQuery for analytics?
// plain

Google BigQuery is a serverless, highly scalable data warehouse that enables you to analyze large datasets quickly and cost-effectively. It can be used for analytics by running SQL queries against your data stored in BigQuery. With BigQuery, you can analyze data stored in tables, views, and external data sources.

For example, you can use the following SQL query to count the number of rows in a table:

```
SELECT COUNT(*)
FROM `mydataset.mytable`
```

## Output example

```
COUNT(*)
1000
```

## Code explanation

- SELECT COUNT(*): This is the keyword used to count the number of rows in the table.
- FROM: This is the keyword used to indicate the source of the data.
- `mydataset.mytable`: This is the name of the table from which the data will be counted.

## Helpful links
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [BigQuery SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

onelinerhub: [How can I use Google BigQuery for analytics?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-for-analytics)