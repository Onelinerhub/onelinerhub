# How can I use Google Big Query to store data?
// plain

Google BigQuery is a serverless, highly scalable, and cost-effective cloud data warehouse that enables you to store and query data using SQL. You can use BigQuery to store data in a structured format, such as CSV, JSON, Avro, or Parquet.

For example, you can use the following code to create a table in BigQuery and store data in it:

```
CREATE TABLE my_dataset.my_table (
  id INT64,
  name STRING,
  age INT64
)

INSERT INTO my_dataset.my_table (id, name, age) VALUES
  (1, 'John', 20),
  (2, 'Jane', 30)
```

This code will create a table called `my_table` in the `my_dataset` dataset, with three columns: `id`, `name`, and `age`. It will then insert two rows of data into the table.

You can also use BigQuery to query your data using SQL. For example, the following code will query the table created above to get the names and ages of all users:

```
SELECT name, age FROM my_dataset.my_table
```

This code will return the following output:

```
John, 20
Jane, 30
```

For more information on using BigQuery to store and query data, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs).

onelinerhub: [How can I use Google Big Query to store data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-to-store-data)