# How do I query Google Big Query?
// plain

Querying Google BigQuery is done through the BigQuery web UI, the bq command-line tool, or the BigQuery REST API.

Using the BigQuery web UI:
1. Log into the [Google Cloud Console](https://console.cloud.google.com/)
2. Select the project you want to query
3. Select **BigQuery** from the left-side navigation menu
4. Select the dataset you want to query
5. Click the **Compose Query** button
6. Enter the SQL query in the Query Editor
7. Click the **Run Query** button

Using the bq command-line tool:
1. Install the [Cloud SDK](https://cloud.google.com/sdk/)
2. Run the command `bq query --use_legacy_sql=false "SELECT * FROM dataset.table"`

Using the BigQuery REST API:
1. Make a POST request to the [query endpoint](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query)
2. Provide the query string in the request body

An example query using the BigQuery web UI:
```
SELECT * FROM dataset.table
```

This query will return all the records in the specified table.

onelinerhub: [How do I query Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-query-google-big-query)