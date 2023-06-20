# How can I export data from Google Big Query to an XLSX file?
// plain

Exporting data from Google Big Query to an XLSX file is possible using the BigQuery Storage API. The steps to do this are as follows:

1. Create a service account with appropriate permissions (BigQuery Admin, BigQuery Data Viewer, and Storage Object Admin)
2. Generate a private key for the service account
3. Create a Google Cloud Storage bucket
4. Create a BigQuery job to export the data from BigQuery to the Google Cloud Storage bucket
5. Use the Storage API to download the file from the Google Cloud Storage bucket to your local machine

Example code for steps 4 and 5:

```
# Step 4
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Set the destination URI of the exported data
destination_uri = 'gs://my-bucket/exported_data.csv'

# Construct a BigQuery Extract Job Config
job_config = bigquery.job.ExtractJobConfig()
job_config.destination_format = bigquery.DestinationFormat.CSV

# Set the destination table
dataset_ref = client.dataset('my_dataset')
table_ref = dataset_ref.table('my_table')

# Start the extraction job
extract_job = client.extract_table(
    table_ref,
    destination_uri,
    job_config=job_config
)
extract_job.result()

# Step 5
from google.cloud import storage

# Create a storage client
storage_client = storage.Client()

# Get the bucket that the file is in
bucket = storage_client.get_bucket('my-bucket')

# Create a blob object from the filepath
source_blob = bucket.blob('exported_data.csv')

# Download the file to a destination
destination_file_name = 'exported_data.xlsx'
source_blob.download_to_filename(destination_file_name)
```

## Helpful links
- [Google Cloud Storage API Documentation](https://cloud.google.com/storage/docs/reference/libraries)
- [BigQuery Storage API Documentation](https://cloud.google.com/bigquery/docs/reference/storage)

onelinerhub: [How can I export data from Google Big Query to an XLSX file?](https://onelinerhub.com/google-big-query/how-can-i-export-data-from-google-big-query-to-an-xlsx-file)