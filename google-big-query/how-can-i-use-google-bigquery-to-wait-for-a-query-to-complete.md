# How can I use Google BigQuery to wait for a query to complete?
// plain

Using Google BigQuery to wait for a query to complete is a simple process.

First, create a job configuration object and set the configuration query property to the query you want to execute:

```
job_config = bigquery.QueryJobConfig()
job_config.query = query_string
```

Next, create a query job and submit it to BigQuery:

```
query_job = bigquery.Client().query(job_config)
```

Finally, wait for the query job to complete and retrieve the results:

```
query_job.result()
```

The `query_job.result()` method will block until the query job is finished and will return a list of results. You can also use the `query_job.done()` method to check if the query job is finished.

The following code snippet shows an example of how to wait for a query job to complete and retrieve the results:

```
from google.cloud import bigquery

# Create a job configuration object and set the configuration query property to the query you want to execute
job_config = bigquery.QueryJobConfig()
job_config.query = query_string

# Create a query job and submit it to BigQuery
query_job = bigquery.Client().query(job_config)

# Wait for the query job to complete and retrieve the results
results = query_job.result()

# Print the results
for row in results:
    print(row)
```

The output will be the results of the query you specified.

## Code explanation


1. `job_config = bigquery.QueryJobConfig()` - Create a job configuration object to specify the query to execute.
2. `job_config.query = query_string` - Set the configuration query property to the query you want to execute.
3. `query_job = bigquery.Client().query(job_config)` - Create a query job and submit it to BigQuery.
4. `query_job.result()` - Wait for the query job to complete and retrieve the results.
5. `for row in results:` - Loop through the results and print each row.

## Helpful links

- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [BigQuery Query Job Configuration](https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.job.QueryJobConfig.html)

onelinerhub: [How can I use Google BigQuery to wait for a query to complete?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-wait-for-a-query-to-complete)