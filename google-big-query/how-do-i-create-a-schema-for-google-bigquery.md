# How do I create a schema for Google BigQuery?
// plain

Creating a schema for Google BigQuery is easy and straightforward. The basic syntax is CREATE TABLE [table_name] (column_name data_type, column_name data_type, ...). To illustrate, here is an example of creating a table with three columns:

```
CREATE TABLE my_table (
  id INT64,
  name STRING,
  age INT64
);
```

The code above will create a table named `my_table` with three columns: `id`, `name`, and `age`. The data type for each column is specified after the column name.

You can also add additional options when creating a table. For example, you can specify the table's expiration time, its partitioning, and its clustering. Further details can be found in the [Google BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language).

For example, the following code creates a table that will expire in 7 days and is partitioned by date:

```
CREATE TABLE my_table (
  id INT64,
  name STRING,
  age INT64,
  date DATE
)
PARTITION BY date
EXPIRATION_TIME 7;
```

The code above will create a table named `my_table` with four columns: `id`, `name`, `age`, and `date`. The table will be partitioned by date and will expire in 7 days.

Creating a schema for Google BigQuery is easy and straightforward. The basic syntax is CREATE TABLE [table_name] (column_name data_type, column_name data_type, ...). You can also add additional options such as expiration time, partitioning, and clustering. Further details can be found in the [Google BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language).

onelinerhub: [How do I create a schema for Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-create-a-schema-for-google-bigquery)