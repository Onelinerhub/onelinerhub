# How do I upload a CSV file to Google BigQuery?
// plain

1. First, create a Google Cloud Storage bucket.
2. Next, use the `bq` command line tool to upload the CSV file to the bucket.
   ```
   bq load --source_format=CSV <dataset>.<table> <csv file> <schema>
   ```
3. Then, create a BigQuery table in the desired dataset.
4. Finally, use the `bq` command line tool to load the CSV file into the table.
   ```
   bq load --source_format=CSV <dataset>.<table> gs://<bucket>/<csv file> <schema>
   ```

The `bq` command line tool can be used to upload a CSV file to Google BigQuery. The command consists of the following parts:
* `bq`: the command line tool
* `load`: the command to load data
* `--source_format=CSV`: the source format of the data (in this case, CSV)
* `<dataset>.<table>`: the destination dataset and table
* `<csv file>`: the CSV file to be uploaded
* `<schema>`: the schema of the table

If the CSV file is stored in a Google Cloud Storage bucket, the `gs://<bucket>/<csv file>` should be used instead of `<csv file>` in the command.

## Helpful links
* [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
* [Google Cloud Storage Documentation](https://cloud.google.com/storage/docs/)

onelinerhub: [How do I upload a CSV file to Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-upload-a-csv-file-to-google-bigquery)