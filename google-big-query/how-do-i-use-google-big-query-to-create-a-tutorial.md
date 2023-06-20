# How do I use Google Big Query to create a tutorial?
// plain

1. First, sign up for a Google Cloud Platform account and enable BigQuery API.
2. Create a new project, and use the BigQuery web UI to create a dataset and table.
3. Use the `bq` command line tool to load data into the table. For example:
```
bq load --source_format=CSV mydataset.mytable gs://mybucket/data.csv
```
4. Use the `bq` command line tool to query the data. For example:
```
bq query --use_legacy_sql=false 'SELECT * FROM `mydataset.mytable`'
```
5. Use the `bq` command line tool to export query results. For example:
```
bq query --use_legacy_sql=false --destination_table=mydataset.mytable_export 'SELECT * FROM `mydataset.mytable`'
```
6. Use the BigQuery web UI to view query results and export them as a CSV file.
7. To learn more about using BigQuery, refer to the [BigQuery Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I use Google Big Query to create a tutorial?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-to-create-a-tutorial)