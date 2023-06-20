# How do I make a request to Google Big Query?
// plain

In order to make a request to Google BigQuery, the following steps should be taken:

1. Authenticate the user and create a BigQuery Client object. This can be done as follows:

```
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()
```

2. Define the query string. This is the SQL query that will be sent to BigQuery.

3. Create a query job. This will allow us to run the query asynchronously.

```
# The name for the query job
job_name = 'my_first_query_job'

# Set up the query
query_job = client.query(query_string, job_name=job_name)
```

4. Run the query job.

```
# Run the query job
query_job.result()
```

5. Get the results.

```
# Get the results
for row in query_job:
    print(row)
```

6. Clean up the query job.

```
# Delete the query job
query_job.delete()
```

7. Close the BigQuery client object.

```
# Close the BigQuery client
client.close()
```

For more information, please refer to the [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I make a request to Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-make-a-request-to-google-big-query)