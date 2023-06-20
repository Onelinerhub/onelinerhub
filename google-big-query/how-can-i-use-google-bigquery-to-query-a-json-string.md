# How can I use Google BigQuery to query a JSON string?
// plain

Google BigQuery is a powerful query engine that can be used to query JSON strings. To use BigQuery to query a JSON string, one must first upload the JSON string to a BigQuery table. This can be done with the `bq` command line tool, or through the BigQuery web UI.

Once the JSON string is uploaded to a BigQuery table, it can be queried using the standard SQL syntax. For example, the following query will return all records in the table:

```SQL
SELECT * FROM `mydataset.mytable`;
```

The output of this query will be a list of records, each of which is a JSON string. To query specific fields from the JSON string, the `JSON_EXTRACT` function can be used. For example, the following query will return the `name` field from each record in the table:

```SQL
SELECT JSON_EXTRACT(record, '$.name') FROM `mydataset.mytable`;
```

The output of this query will be a list of the `name` fields from each record.

In addition to querying JSON strings, BigQuery can also be used to manipulate JSON strings. This can be done using the `JSON_EXTRACT_SCALAR` and `JSON_SET` functions. For example, the following query will update the `name` field of all records in the table to `John Doe`:

```SQL
UPDATE `mydataset.mytable`
SET record = JSON_SET(record, '$.name', 'John Doe');
```

For more information on how to use BigQuery to query and manipulate JSON strings, please refer to the [BigQuery JSON Functions documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions).

onelinerhub: [How can I use Google BigQuery to query a JSON string?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-query-a-json-string)