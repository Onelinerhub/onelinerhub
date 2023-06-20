# How do I download a Google Big Query logo in PNG format?
// plain

1. To download a Google Big Query logo in PNG format, go to the [Google Cloud Platform Console](https://console.cloud.google.com/).
2. On the left side of the page, select **BigQuery**.
3. In the top right corner, click on the **Logo** icon.
4. A drop-down menu will appear. Select **Download logo**.
5. A dialogue box will appear. Select **PNG** from the drop-down menu.
6. Click **Download** to save the logo to your computer.
7. You can now use the logo in your project.

## Example code

```
# Download the BigQuery logo
from google.cloud import storage

# Create a storage client
storage_client = storage.Client()

# Get the logo bucket
bucket = storage_client.get_bucket('bigquery-public-data')

# Create a blob from the filepath
blob = bucket.blob('logos/bigquery_logo_rgb.png')

# Download the file
blob.download_to_filename('bigquery_logo_rgb.png')
```

Output (if any):

No output.

## Code explanation


* `from google.cloud import storage`: imports the Google Cloud Storage library.
* `storage_client = storage.Client()`: instantiates the Storage Client.
* `bucket = storage_client.get_bucket('bigquery-public-data')`: fetches the bucket containing the BigQuery logo.
* `blob = bucket.blob('logos/bigquery_logo_rgb.png')`: creates a blob object from the filepath.
* `blob.download_to_filename('bigquery_logo_rgb.png')`: downloads the file to the specified filename.

## Helpful links

* [Google Cloud Platform Console](https://console.cloud.google.com/)

onelinerhub: [How do I download a Google Big Query logo in PNG format?](https://onelinerhub.com/google-big-query/how-do-i-download-a-google-big-query-logo-in-png-format)