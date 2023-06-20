# How can I use Google Big Query to store and manage my NoSQL data?
// plain

Google BigQuery is a powerful cloud-based data warehouse that can be used to store and manage NoSQL data. It supports a wide range of data formats, including JSON, Avro and CSV. To store and manage NoSQL data in BigQuery, you can use the BigQuery service to create a table and load the data into it.

For example, the following code creates a table called “my_table” in BigQuery and loads a JSON file into it:

```
bq --location=US mk --table --schema my_table.json my_table
bq load --source_format=NEWLINE_DELIMITED_JSON my_table.json gs://my-bucket/my_file.json
```

The first command creates the table, while the second command loads the JSON file into the table.

In addition, BigQuery includes a SQL-like query language called BigQuery SQL, which can be used to query and analyze the data stored in BigQuery. For example, the following query counts the number of records in the table:

```
SELECT COUNT(*) FROM my_table
```

## Output example


```
+-------+
|  f0_  |
+-------+
| 10000 |
+-------+
```

The query language also supports a wide range of operations, such as joins, aggregation, and window functions.

## Helpful links

- [BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [BigQuery Query Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

onelinerhub: [How can I use Google Big Query to store and manage my NoSQL data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-to-store-and-manage-my-nosql-data)