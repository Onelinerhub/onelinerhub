# How can I use Google BigQuery to access Wikipedia data?
// plain

Google BigQuery is a powerful tool for analyzing large datasets stored in the cloud. You can use BigQuery to access and analyze data from Wikipedia. To do this, you need to first create a BigQuery dataset, which is a collection of tables. You can then use the BigQuery API to query the data from Wikipedia.

For example, the following code will query Wikipedia to get the page titles for all pages in the English Wikipedia:

```
SELECT page_title
FROM `bigquery-public-data.wikipedia.page`
WHERE wiki_db = "enwiki"
```

The output of this query will be a list of all page titles in the English Wikipedia.

The code consists of three parts:

1. The `SELECT` statement, which specifies which columns to include in the output.
2. The `FROM` clause, which specifies the table to query.
3. The `WHERE` clause, which specifies the criteria for the query.

For more information on how to use BigQuery to access Wikipedia data, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/wikipedia).

onelinerhub: [How can I use Google BigQuery to access Wikipedia data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-access-wikipedia-data)