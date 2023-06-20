# How do I use Google Big Query?
// plain

Google BigQuery is a fully managed, serverless data warehouse that lets you store and query massive datasets quickly and cost-effectively. It is a part of the Google Cloud Platform (GCP).

To use Google BigQuery, you first need to create a project in the [Google Cloud Console](https://console.cloud.google.com/). Once you have created a project, you can use the BigQuery web UI or the command-line tool to create datasets, tables, and load data into them.

You can also query data using the BigQuery web UI, the command-line tool, or the BigQuery API. Here is an example of querying data using the BigQuery API:

```
# Imports the Google Cloud client library
from google.cloud import bigquery

# Instantiates a client
client = bigquery.Client()

# The name for the dataset
dataset_name = 'my_new_dataset'

# Prepares a reference to the new dataset
dataset_ref = client.dataset(dataset_name)

# Creates the new dataset
dataset = bigquery.Dataset(dataset_ref)
dataset = client.create_dataset(dataset)

print('Dataset {} created.'.format(dataset.dataset_id))
```

## Output example

```
Dataset my_new_dataset created.
```

The code above:

1. Imports the Google Cloud client library
2. Instantiates a client
3. Sets the dataset name
4. Prepares a reference to the new dataset
5. Creates the new dataset
6. Prints a success message

For more information on using BigQuery, please see the [BigQuery Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I use Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-1687226203)