# How can I use Google BigQuery BI Engine to analyze large datasets?
// plain

Google BigQuery BI Engine is a serverless, in-memory analysis service that allows you to analyze large datasets using SQL. It provides an interactive query interface that lets you quickly upload and analyze data in BigQuery.

Example code to analyze a large dataset using BigQuery BI Engine:
```
# Standard SQL
SELECT
    COUNT(*)
FROM
    `bigquery-public-data.samples.natality`
```
## Output example

```
Row count: 5642088
```

## Code explanation

1. `SELECT COUNT(*)`: This statement is used to count the total number of rows in the dataset.
2. `FROM `bigquery-public-data.samples.natality`: This statement is used to specify the dataset to be analyzed.

## Helpful links
- [Google BigQuery BI Engine Documentation](https://cloud.google.com/bigquery/docs/bqml-intro)
- [BigQuery ML Tutorial](https://cloud.google.com/bigquery-ml/docs/tutorials/bqml-tutorial)

onelinerhub: [How can I use Google BigQuery BI Engine to analyze large datasets?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-bi-engine-to-analyze-large-datasets)