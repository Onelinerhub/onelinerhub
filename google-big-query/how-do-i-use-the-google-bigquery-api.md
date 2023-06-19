# How do I use the Google BigQuery API?
// plain

Using the Google BigQuery API is a great way to access and analyze data stored in BigQuery.

To get started, you will need to create a project in the Google Cloud Platform Console and enable the BigQuery API.

Once the BigQuery API is enabled, you can use the [Google BigQuery client library for Python](https://cloud.google.com/bigquery/docs/reference/libraries) to access the API.

The following example shows how to use the BigQuery client library to list the datasets in your project:

```
from google.cloud import bigquery

client = bigquery.Client()

datasets = list(client.list_datasets())

dataset_references = [dataset.reference for dataset in datasets]

print(dataset_references)
```

The output of this code will be a list of the dataset references in your project.

To use BigQuery to query data, you can use the [BigQuery Python client library](https://cloud.google.com/bigquery/docs/reference/libraries) to create a query job.

The following example shows how to use the BigQuery client library to query a table in your project:

```
from google.cloud import bigquery

client = bigquery.Client()

query = """
    SELECT *
    FROM `project.dataset.table`
    LIMIT 10
"""

query_job = client.query(query)

for row in query_job:
    print(row)
```

The output of this code will be a list of the rows from the table you queried.

For more information on using the BigQuery API, see the [BigQuery Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I use the Google BigQuery API?](https://onelinerhub.com/google-big-query/how-do-i-use-the-google-bigquery-api)