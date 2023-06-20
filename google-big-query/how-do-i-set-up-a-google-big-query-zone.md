# How do I set up a Google Big Query zone?
// plain

1. To set up a Google Big Query zone, you will need to create a project in the Google Cloud Platform Console.
2. Once the project is created, you can open the BigQuery page from the left-hand side menu.
3. Click the “Create Dataset” button to create a new dataset.
4. Enter a name for the dataset, select a location, and click the “Create Dataset” button.
5. You can now create tables in the dataset. To do this, click the “Create Table” button and enter a name for the table.
6. Select the type of data you want to store in the table and click “Create Table”.
7. You can now query the data stored in the table using the BigQuery Query Editor.

## Example code

```
SELECT *
FROM [project-name:dataset-name.table-name]
```

## Output example

```
Query Results
col1	col2
value1	value2
value3	value4
```

## Code explanation

- `SELECT *` - This statement is used to select all columns from the specified table.
- `FROM [project-name:dataset-name.table-name]` - This statement is used to specify the project, dataset, and table from which the data is to be retrieved.

## Helpful links
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [BigQuery Query Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

onelinerhub: [How do I set up a Google Big Query zone?](https://onelinerhub.com/google-big-query/how-do-i-set-up-a-google-big-query-zone)