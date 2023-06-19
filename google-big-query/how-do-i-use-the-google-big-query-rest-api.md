# How do I use the Google Big Query REST API?
// plain

The Google BigQuery REST API allows you to interact with BigQuery programmatically. This can be done by making HTTP requests to the API endpoints.

To use the BigQuery REST API, you need to first authenticate using a service account. This can be done by creating a service account in the Google Cloud Platform Console and downloading the JSON file.

Once the authentication is set up, you can make requests to the BigQuery API. For example, the following code block uses the Google API Client Library for Python to make a request to the BigQuery API:

```python
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Make an API request.
datasets = list(client.list_datasets())

# Print results.
print("Datasets:")
for dataset in datasets:
    print("\t{}".format(dataset.dataset_id))
```

## Output example

```
Datasets:
    my_dataset
    another_dataset
```

## Code explanation

1. `from google.cloud import bigquery` - imports the BigQuery library
2. `client = bigquery.Client()` - creates a BigQuery Client object
3. `datasets = list(client.list_datasets())` - makes a request to the BigQuery API to list datasets
4. `print("Datasets:")` - prints the header for the output
5. `for dataset in datasets:` - iterates over the list of datasets
6. `print("\t{}".format(dataset.dataset_id))` - prints the dataset ID

## Helpful links
- [Google BigQuery REST API](https://cloud.google.com/bigquery/docs/reference/rest/)
- [Google BigQuery Client Libraries](https://cloud.google.com/bigquery/docs/reference/libraries)

onelinerhub: [How do I use the Google Big Query REST API?](https://onelinerhub.com/google-big-query/how-do-i-use-the-google-big-query-rest-api)