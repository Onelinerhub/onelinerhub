# How do I use a Google BigQuery URL?
// plain

Using a Google BigQuery URL is a great way to access data stored in BigQuery. To use a BigQuery URL, you'll need to have a valid BigQuery project, dataset, and table.

First, you'll need to construct your BigQuery URL. The format of the URL is `https://bigquery.cloud.google.com/<project_id>/<dataset_name>/<table_name>`.

Once you have the URL, you can use the BigQuery command line tool to run a query against the table. For example, the following command will query the `my_table` table in the `my_dataset` dataset in the `my_project` project:

```
bq query --use_legacy_sql=false 'SELECT * FROM my_project.my_dataset.my_table'
```

The query will return the contents of the table in the form of a list of records.

You can also use the BigQuery web UI to view the data stored in a table. To do this, simply navigate to the URL you constructed and you'll be able to view the data in the table.

## Helpful links

- [BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [BigQuery Command Line Tool](https://cloud.google.com/sdk/gcloud/reference/bq/query)

onelinerhub: [How do I use a Google BigQuery URL?](https://onelinerhub.com/google-big-query/how-do-i-use-a-google-bigquery-url)