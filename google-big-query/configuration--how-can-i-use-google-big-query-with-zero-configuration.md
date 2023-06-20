# configuration

How can I use Google Big Query with zero configuration?
// plain

Google Big Query is an enterprise data warehouse that enables organizations to analyze data quickly and cost-effectively. To use Google Big Query with zero configuration, you can use the [Google Cloud Console](https://console.cloud.google.com/bigquery). This will allow you to create datasets, query data, and manage resources without any additional configuration.

To get started with Google Big Query, you can use the following example code:

```
# Imports the Google Cloud client library
from google.cloud import bigquery

# Instantiates a client
bigquery_client = bigquery.Client()

# The name for the new dataset
dataset_id = 'my_new_dataset'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)

# Creates the new dataset
dataset = bigquery.Dataset(dataset_ref)

# Creates the new dataset
dataset = bigquery_client.create_dataset(dataset)

print('Dataset {} created.'.format(dataset.dataset_id))
```

The output of the code should look like this:
```
Dataset my_new_dataset created.
```

The code above does the following:

1. Imports the Google Cloud client library, which is necessary for using Google Big Query.
2. Instantiates a client, which is used to create a dataset.
3. Sets the name for the new dataset.
4. Prepares a reference to the new dataset.
5. Creates the new dataset.
6. Prints a message that the dataset was created.

Using Google Big Query with zero configuration is simple and easy. With just a few lines of code, you can get started with Google Big Query and start analyzing data quickly and cost-effectively.

onelinerhub: [configuration

How can I use Google Big Query with zero configuration?](https://onelinerhub.com/google-big-query/configuration--how-can-i-use-google-big-query-with-zero-configuration)