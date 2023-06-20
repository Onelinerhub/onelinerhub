# How can I use Google BigQuery to retrieve data from a specific year?
// plain

Google BigQuery is a cloud-based data warehousing service that can be used to query and retrieve data from a specific year.

To use BigQuery to retrieve data from a specific year, you can use the `WHERE` clause with the `YEAR` function. For example, the following query will return data from the year 2020:

```
SELECT *
FROM my_dataset.my_table
WHERE YEAR(date_column) = 2020
```

The `WHERE` clause is used to filter the data returned from the query, and the `YEAR` function is used to extract the year from the `date_column` and filter it to only return data from the year 2020.

## Code explanation


* `SELECT` - used to specify the columns to be returned from the query
* `FROM` - used to specify the dataset and table to query
* `WHERE` - used to filter the data returned from the query
* `YEAR` - used to extract the year from the `date_column`

## Helpful links

* [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)
* [SQL Clauses](https://cloud.google.com/bigquery/docs/reference/standard-sql/clauses)
* [SQL Functions](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)

onelinerhub: [How can I use Google BigQuery to retrieve data from a specific year?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-retrieve-data-from-a-specific-year)