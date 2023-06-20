# How do I use Google BigQuery on Google Cloud Platform?
// plain

Google BigQuery is a cloud-based data warehouse that allows users to store and query large datasets. To use BigQuery on Google Cloud Platform, you will need to create a project and enable the BigQuery API.

Once the API is enabled, you can use the BigQuery web UI, the command-line tool, or the BigQuery client libraries for your preferred language to interact with BigQuery.

For example, to run a query with the BigQuery command-line tool, you can use the following command:

```
bq query --use_legacy_sql=false 'SELECT * FROM `my-project.mydataset.mytable`'
```

The output of this command will be the result of the query:

```
+------+--------+
| Col1 | Col2   |
+------+--------+
| 1    | hello  |
| 2    | world  |
+------+--------+
```

The code above consists of the following parts:

1. `bq query` - the command for running a query;
2. `--use_legacy_sql=false` - the flag to indicate that the query should use standard SQL;
3. `SELECT * FROM `my-project.mydataset.mytable`'` - the query itself.

For more information, please refer to the [BigQuery documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I use Google BigQuery on Google Cloud Platform?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-on-google-cloud-platform)