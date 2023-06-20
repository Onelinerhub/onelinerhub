# How do I use Google Big Query to zip files?
// plain

Google BigQuery does not natively support zipping files. To use BigQuery to zip files, you will need to export the files to Google Cloud Storage, then use the gsutil command line tool to zip the files.

The following example code will export the file named `my_file.csv` from BigQuery to Google Cloud Storage, then zip the file:

```
bq extract --destination_format=CSV 'my-project:my-dataset.my_table' gs://my-bucket/my_file.csv
gsutil cp gs://my-bucket/my_file.csv gs://my-bucket/my_file.zip
```

This code will create a zip file named `my_file.zip` in the Google Cloud Storage bucket `my-bucket`.

The code consists of two parts:
1. `bq extract`: This command will export the table `my-project:my-dataset.my_table` from BigQuery to the file `my_file.csv` in the Google Cloud Storage bucket `my-bucket`.
2. `gsutil cp`: This command will copy the file `my_file.csv` from the Google Cloud Storage bucket `my-bucket` to the file `my_file.zip` in the same bucket.

For more information about the `bq extract` and `gsutil cp` commands, see the following links:
- [bq extract](https://cloud.google.com/bigquery/docs/exporting-data)
- [gsutil cp](https://cloud.google.com/storage/docs/gsutil/commands/cp)

onelinerhub: [How do I use Google Big Query to zip files?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-to-zip-files)