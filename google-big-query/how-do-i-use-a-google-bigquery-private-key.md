# How do I use a Google BigQuery private key?
// plain

A Google BigQuery private key is used to authenticate users when they access the BigQuery API. It is a JSON file that contains private credentials that are used to authenticate a user.

In order to use a Google BigQuery private key, you need to first download the JSON file from the Google Cloud Console. Once the file is downloaded, you can use the following code snippet to authenticate with BigQuery:

```
# Imports the Google Cloud client library
from google.cloud import bigquery

# The path to the JSON file containing your private key
private_key_path = '<PATH_TO_JSON_FILE>'

# Instantiates a client
client = bigquery.Client.from_service_account_json(private_key_path)
```

The code snippet above will create a `client` object that can be used to interact with BigQuery.

## Code explanation

1. `from google.cloud import bigquery`: imports the Google Cloud client library
2. `private_key_path = '<PATH_TO_JSON_FILE>'`: sets the path to the JSON file containing your private key
3. `client = bigquery.Client.from_service_account_json(private_key_path)`: instantiates a client object

## Helpful links
- [Authenticate with a service account](https://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python)
- [BigQuery API Client Libraries](https://cloud.google.com/bigquery/docs/reference/libraries)

onelinerhub: [How do I use a Google BigQuery private key?](https://onelinerhub.com/google-big-query/how-do-i-use-a-google-bigquery-private-key)