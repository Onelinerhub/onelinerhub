# How do I format data for use in Google BigQuery?
// plain

Google BigQuery is a powerful cloud-based data warehouse that allows users to store and query large datasets. To use data in BigQuery, it must be formatted in a specific way. The best way to format data for BigQuery is to use the BigQuery Data Transfer Service (DTS). This service allows you to easily load data from a variety of sources, including Google Cloud Storage, Google Drive, and Google Sheets.

For example, if you have a CSV file stored in Google Cloud Storage, you can use the following code to load it into BigQuery:

```
# Imports the Google Cloud client library
from google.cloud import bigquery

# Instantiates a client
bigquery_client = bigquery.Client()

# The name for the new dataset
dataset_id = 'my_new_dataset'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)

# Creates the new dataset
dataset = bigquery_client.create_dataset(dataset)

# The name for the new table
table_id = 'my_new_table'

# Prepares a reference to the new table
table_ref = dataset_ref.table(table_id)
table = bigquery.Table(table_ref)

# Configures the schema of the table
schema = [
    bigquery.SchemaField('name', 'STRING'),
    bigquery.SchemaField('age', 'INTEGER')
]
table.schema = schema

# Creates the new table
table = bigquery_client.create_table(table)

# Configures the load job
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.autodetect = True

# The source file for the load job
uri = 'gs://my-bucket/data.csv'

# Loads the CSV file into the table
load_job = bigquery_client.load_table_from_uri(
    uri, table_ref, job_config=job_config
)

# Waits for the load job to complete
load_job.result()
```

This code will create a new BigQuery dataset and table, configure the schema of the table, and then load the CSV file from Google Cloud Storage into the table.

## Code explanation


1. `from google.cloud import bigquery`: imports the Google Cloud client library.
2. `dataset_id = 'my_new_dataset'`: sets the name for the new dataset.
3. `dataset_ref = bigquery_client.dataset(dataset_id)`: prepares a reference to the new dataset.
4. `dataset = bigquery_client.create_dataset(dataset)`: creates the new dataset.
5. `table_id = 'my_new_table'`: sets the name for the new table.
6. `table_ref = dataset_ref.table(table_id)`: prepares a reference to the new table.
7. `schema = [bigquery.SchemaField('name', 'STRING'), bigquery.SchemaField('age', 'INTEGER')]`: configures the schema of the table.
8. `table.schema = schema`: sets the schema of the table.
9. `table = bigquery_client.create_table(table)`: creates the new table.
10. `job_config = bigquery.LoadJobConfig()`: configures the load job.
11. `job_config.source_format = bigquery.SourceFormat.CSV`: sets the source format of the load job to CSV.
12. `job_config.skip_leading_rows = 1`: skips the first row of the CSV file.
13. `job_config.autodetect = True`: enables autodetection of the data types in the CSV file.
14. `uri = 'gs://my-bucket/data.csv'`: sets the source file for the load job.
15. `load_job = bigquery_client.load_table_from_uri(uri, table_ref, job_config=job_config)`: loads the CSV file into the table.
16. `load_job.result()`: waits for the load job to complete.

## Helpful links

- [BigQuery Data Transfer Service](https://cloud.google.com/bigquery/docs/reference/data-transfer-service)
- [Loading Data into BigQuery](https://cloud.google.com/bigquery/docs/loading-data)

onelinerhub: [How do I format data for use in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-format-data-for-use-in-google-bigquery)