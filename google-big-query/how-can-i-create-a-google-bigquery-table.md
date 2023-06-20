# How can I create a Google BigQuery table?
// plain

Creating a Google BigQuery table is a simple process.

First, you must have a Google Cloud Platform account and be signed in to the Google Cloud Console.

Once logged in, you can create a new dataset by navigating to the BigQuery web UI.

To create a new table, you must specify a dataset to contain the table and provide a table name.

You can also optionally specify a schema, which defines the table structure.

For example, the following code creates a new table called `my_table` in a dataset called `my_dataset`:
```
#standardSQL
CREATE TABLE my_dataset.my_table (
  id INT64,
  name STRING
);
```

The schema defines two columns, `id` and `name`, with data types of `INT64` and `STRING` respectively.

Once the table is created, you can insert data into it, query it, and perform other operations.

## Helpful links
* [Creating a Table](https://cloud.google.com/bigquery/docs/tables#create-table)
* [Data Types](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)

onelinerhub: [How can I create a Google BigQuery table?](https://onelinerhub.com/google-big-query/how-can-i-create-a-google-bigquery-table)