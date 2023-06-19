# How do I use Google Big Query to create a database?
// plain

Google BigQuery is a cloud-based data warehouse that enables users to store and query massive datasets using SQL. To create a database in BigQuery, you must first create a dataset. A dataset is a grouping of tables that share the same access control, expiration time, and other properties.

To create a dataset, you can use the BigQuery web UI, the command-line tool, or the BigQuery API.

For example, to create a dataset using the BigQuery web UI, you can follow these steps:

1. Log into the Google Cloud Console and navigate to the BigQuery page.
2. Click the “Create Dataset” button.
3. Enter a name for the dataset.
4. Select a data location.
5. Select a default table expiration time.
6. Click the “Create Dataset” button to create the dataset.

You can also use the command-line tool or the BigQuery API to create a dataset. For example, the following command creates a dataset using the bq command-line tool:

```
bq mk --dataset my_dataset
```

The output of the command will be:

```
Dataset 'my_project:my_dataset' successfully created.
```

Once the dataset has been created, you can create tables within the dataset. Tables are the basic unit of data storage in BigQuery.

## Helpful links

- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Creating Datasets](https://cloud.google.com/bigquery/docs/datasets#create-dataset)
- [Using the bq Command-line Tool](https://cloud.google.com/bigquery/docs/bq-command-line-tool)

onelinerhub: [How do I use Google Big Query to create a database?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-to-create-a-database)