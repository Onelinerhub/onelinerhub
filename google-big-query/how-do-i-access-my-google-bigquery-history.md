# How do I access my Google BigQuery history?
// plain

Accessing your Google BigQuery history is easy.

To access your BigQuery history, you will need to log into the [BigQuery web UI](https://console.cloud.google.com/bigquery).

Once logged in, click on the “History” tab at the top of the page. This will take you to a page that lists all of your recent BigQuery jobs.

You can also access your BigQuery history programmatically by using the [BigQuery API](https://cloud.google.com/bigquery/docs/reference/rest/).

For example, to list all of your recent jobs, you can use the following code:

```
# Imports the Google Cloud client library
from google.cloud import bigquery

# Instantiates a client
bigquery_client = bigquery.Client()

# Lists all jobs
jobs = list(bigquery_client.list_jobs())

# Prints the jobs
for job in jobs:
    print(job.name)
```

The output of the above code would be a list of your recent jobs, such as:

```
job_zk6jZvJjV1m9u9hfS5f_x2YqFgw
job_U3Bzp_6UyPfF5ZF-V_Q7hgLb7M
job_6G-X2y2QW9qmf6NyQ1PQV6e3tHo
```

You can also use the BigQuery API to get more detailed information about each job, such as when it was executed, how much data it processed, and how long it took to complete.

## Helpful links

- [BigQuery web UI](https://console.cloud.google.com/bigquery)
- [BigQuery API](https://cloud.google.com/bigquery/docs/reference/rest/)

onelinerhub: [How do I access my Google BigQuery history?](https://onelinerhub.com/google-big-query/how-do-i-access-my-google-bigquery-history)