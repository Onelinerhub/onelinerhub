# How do I use the syntax of Google Big Query?
// plain

Google BigQuery is a serverless, highly scalable, and cost-effective cloud data warehouse. It supports a wide range of standard SQL syntax, making it easy to query data stored in BigQuery.

The following is an example of the syntax used to query a table in BigQuery:

```
SELECT *
FROM `project-name.dataset-name.table-name`
```

This query will return all the columns and rows from the specified table.

You can also use the WHERE clause to filter the results:

```
SELECT *
FROM `project-name.dataset-name.table-name`
WHERE column_name = 'value'
```

This query will return all the columns and rows from the specified table, but only those rows that have `column_name` set to `value`.

You can also use the GROUP BY clause to aggregate the results:

```
SELECT column_name, COUNT(*)
FROM `project-name.dataset-name.table-name`
GROUP BY column_name
```

This query will return a count of the number of rows for each unique value of `column_name`.

You can also use the ORDER BY clause to sort the results:

```
SELECT *
FROM `project-name.dataset-name.table-name`
ORDER BY column_name
```

This query will return all the columns and rows from the specified table, sorted in ascending order by `column_name`.

For more information on using the syntax of Google BigQuery, please refer to the following links:

* [Query Syntax Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
* [Data Manipulation Language Syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax)
* [Data Definition Language Syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/ddl-syntax)

onelinerhub: [How do I use the syntax of Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-use-the-syntax-of-google-big-query)