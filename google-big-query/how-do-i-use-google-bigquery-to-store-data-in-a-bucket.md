# How do I use Google BigQuery to store data in a bucket?
// plain

You can use Google BigQuery to store data in a bucket by creating a table in a dataset. To do this, you can run the following command in the BigQuery console:

```
bq mk --table --schema <schema> <dataset>.<table>
```

This command will create a table in the specified dataset, with the schema provided.

You can then use the `bq load` command to load data into the table from a CSV file or from Google Cloud Storage. For example, to load data from a CSV file stored in Cloud Storage:

```
bq load --source_format=CSV <dataset>.<table> <bucket>/<file> <schema>
```

This command will load the data from the specified file into the table, using the specified schema.

The parts of the command are as follows:
1. `bq load`: the command to load data into BigQuery
2. `--source_format=CSV`: the format of the source data (in this case, CSV)
3. `<dataset>.<table>`: the name of the dataset and table to load the data into
4. `<bucket>/<file>`: the location of the file in Cloud Storage
5. `<schema>`: the schema of the data

For more information, refer to the [BigQuery documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I use Google BigQuery to store data in a bucket?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-to-store-data-in-a-bucket)