# How do I use Google Big Query?
// plain

Google BigQuery is a data warehouse service that enables super-fast SQL queries against large datasets. To use BigQuery, you first need to set up a project in the [Google Cloud Console](https://console.cloud.google.com/).

Once you have a project, you can start running queries. Here's an example of a query that will count the number of records in a given table:

```
SELECT COUNT(*)
FROM `bigquery-public-data.samples.shakespeare`
```

This query will return the output:

```
Row	COUNT
1	164656
```

The code consists of three parts:

1. **SELECT COUNT(*)** - This is the command to count the number of records in the table.
2. **FROM** - This specifies the table from which the records should be counted.
3. **`bigquery-public-data.samples.shakespeare`** - This is the name of the table from which the records should be counted.

For more information about using BigQuery, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs).

onelinerhub: [How do I use Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query)