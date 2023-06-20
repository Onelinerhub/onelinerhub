# How do I use Google BigQuery to run an example query?
// plain

1. First, create a Google Cloud Platform account if you don't have one already.
2. Log into the [Google Cloud Platform Console](https://console.cloud.google.com/home/dashboard) and create a new project.
3. Select BigQuery from the navigation menu on the left and click on the “Try BigQuery” button.
4. Select your project from the dropdown menu.
5. Create a new dataset by clicking the “Create Dataset” button.
6. Once the dataset is created, you can upload data to it or run a query.
7. To run a query, click the “Compose Query” button and enter your SQL query in the query editor.

## Example code

```
SELECT *
FROM `mydataset.mytable`
```

## Output example

```
+-------------+------------+-------------+
| column1     | column2    | column3     |
+-------------+------------+-------------+
| value1      | value2     | value3      |
| value4      | value5     | value6      |
+-------------+------------+-------------+
```

## Code explanation

- `SELECT *`: This statement is used to select all the columns in the table.
- `FROM`: This statement is used to specify the table from which the query will be run.
- `mydataset.mytable`: This is the name of the dataset and table that the query is being run on.

## Helpful links
- [Getting Started with BigQuery](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui)
- [BigQuery Query Syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

onelinerhub: [How do I use Google BigQuery to run an example query?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-to-run-an-example-query)