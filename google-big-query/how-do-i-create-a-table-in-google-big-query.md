# How do I create a table in Google Big Query?
// plain

Creating a table in Google Big Query is a simple process.

First, you will need to create a dataset in which to store the table. This can be done by running the following command:

```
bq mk <dataset-name>
```

Once the dataset is created, you can create the table by running the following command:

```
bq mk --table <dataset-name>.<table-name> <schema-file>
```

The `schema-file` is a JSON file that contains the schema for the table. The schema defines the columns and data types for the table.

For example, the following schema file:

```
{
  "fields": [
    {
      "name": "name",
      "type": "STRING"
    },
    {
      "name": "age",
      "type": "INTEGER"
    }
  ]
}
```

would create a table with two columns, `name` and `age`, with the `name` column being a string and the `age` column being an integer.

Once the command is run, the table will be created in the specified dataset.

## Helpful links
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [Creating Tables](https://cloud.google.com/bigquery/docs/tables#creating_a_table)

onelinerhub: [How do I create a table in Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-create-a-table-in-google-big-query)