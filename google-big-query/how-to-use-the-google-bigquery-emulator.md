# How to use the Google BigQuery emulator?
// plain

The Google BigQuery emulator is a local version of the Google BigQuery service that allows you to develop and test your queries without using the cloud. The emulator is available in the Google Cloud SDK and can be used with the BigQuery command-line tool.

To use the Google BigQuery emulator, you need to install the Google Cloud SDK and enable the BigQuery API.

Once the SDK is installed, you can start the emulator by running the following command:
```
gcloud beta emulators bigquery start
```

After starting the emulator, you can run your queries against the emulator using the BigQuery command-line tool. To do this, you need to set the environment variable `BIGQUERY_EMULATOR_HOST` to the host and port of the emulator. For example:

```
export BIGQUERY_EMULATOR_HOST=localhost:8601
```

Once the environment variable is set, you can run your BigQuery queries as you normally would. For example:
```
bq query --use_legacy_sql=false 'SELECT * FROM [mydataset.mytable]'
```

The emulator also supports streaming inserts, which can be used to insert records into a table. To stream records into a table, you need to set the `BIGQUERY_DATASET` environment variable to the dataset you want to stream into. For example:

```
export BIGQUERY_DATASET=mydataset
```

You can then stream records into a table by using the `bq insert` command. For example:
```
bq insert mydataset.mytable mydata.json
```

## Helpful links
- [Google Cloud SDK](https://cloud.google.com/sdk/)
- [BigQuery Command-line Tool](https://cloud.google.com/bigquery/docs/reference/bq-cli-reference)
- [Streaming Data into BigQuery](https://cloud.google.com/bigquery/streaming-data-into-bigquery)

onelinerhub: [How to use the Google BigQuery emulator?](https://onelinerhub.com/google-big-query/how-to-use-the-google-bigquery-emulator)