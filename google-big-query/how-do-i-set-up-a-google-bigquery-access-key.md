# How do I set up a Google BigQuery access key?
// plain

1. To set up a Google BigQuery access key, you will need to create a service account.
2. Go to the [Google Cloud Platform Console](https://console.cloud.google.com/), select the project you want to use, and open the **IAM & Admin** page.
3. Click the **+ CREATE SERVICE ACCOUNT** button at the top of the page.
4. Enter a name and description for the service account, and select **Furnish a new private key**.
5. Select the **JSON** key type.
6. Click **Create**. A JSON key file will be downloaded to your computer.
7. You can use the credentials in the JSON key file to authenticate to BigQuery.

Example code block:
```
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client.from_service_account_json('/path/to/key.json')
```

## Code explanation

- `from google.cloud import bigquery`: imports the BigQuery client library
- `client = bigquery.Client.from_service_account_json('/path/to/key.json')`: creates a BigQuery client object from the credentials in the JSON key file

## Helpful links
- [Google Cloud Platform Console](https://console.cloud.google.com/)
- [BigQuery Client Libraries](https://cloud.google.com/bigquery/docs/reference/libraries)

onelinerhub: [How do I set up a Google BigQuery access key?](https://onelinerhub.com/google-big-query/how-do-i-set-up-a-google-bigquery-access-key)