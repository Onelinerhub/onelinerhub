# How do I export data from Google Big Query?
// plain

Exporting data from Google BigQuery is a straightforward process.

The following example code can be used to export a query result to a file in Google Cloud Storage:

```
bq query --use_legacy_sql=false
--destination_table=mydataset.mytable
"SELECT * FROM mydataset.mytable"
--allow_large_results
--replace
--noflatten_results
--destination_format=FORMAT_AVRO
```

## Code explanation


- `bq query` : The command to run a query in BigQuery.
- `--use_legacy_sql=false` : Specifies that we are using the BigQuery Standard SQL dialect.
- `--destination_table=mydataset.mytable` : The BigQuery table that will store the query result.
- `SELECT * FROM mydataset.mytable` : The query to run.
- `--allow_large_results` : Allows the query to return large result sets.
- `--replace` : Replaces the existing table if it exists.
- `--noflatten_results` : Prevents the query from flattening query results.
- `--destination_format=FORMAT_AVRO` : Specifies the format of the exported data.

The output of this command will be the number of rows processed.

For more information on exporting data from BigQuery, please refer to the [BigQuery documentation](https://cloud.google.com/bigquery/docs/exporting-data).

onelinerhub: [How do I export data from Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-export-data-from-google-big-query)