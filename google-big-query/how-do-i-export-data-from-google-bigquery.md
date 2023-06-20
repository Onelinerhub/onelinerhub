# How do I export data from Google BigQuery?
// plain

Exporting data from Google BigQuery is easy and can be done with a few simple steps.

1. Create a query to retrieve the data you want to export. For example, the following query will export all data from the table named `my_table`:
```
SELECT *
FROM `my_table`
```

2. Run the query in BigQuery.

3. Click the **Export** button in the top right corner of the query results.

4. Select the destination for the exported data. You can export to Google Cloud Storage, Google Drive, or a local file.

5. If you are exporting to a local file, select the file format you want. You can choose from CSV, JSON, or Avro.

6. Click the **Export** button to export the data.

7. If you are exporting to a local file, the file will be downloaded to your computer.

For more information on exporting data from BigQuery, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/exporting-data).

onelinerhub: [How do I export data from Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-export-data-from-google-bigquery)