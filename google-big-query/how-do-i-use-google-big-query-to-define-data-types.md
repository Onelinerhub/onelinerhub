# How do I use Google Big Query to define data types?
// plain

Google BigQuery is a powerful cloud-based data warehouse solution that allows users to define data types. Data types are used to specify the type of data that is stored in a column. The following example code demonstrates how to define data types in BigQuery:

```
# Standard SQL
CREATE TABLE my_table (
  id INT64,
  name STRING,
  age INT64
)
```

The code creates a table called `my_table` with three columns: `id`, `name`, and `age`. The code specifies that the `id` column is of type `INT64`, the `name` column is of type `STRING`, and the `age` column is of type `INT64`.

## Code explanation

- `CREATE TABLE`: This part of the code creates a table.
- `my_table`: This is the name of the table being created.
- `id INT64`: This part of the code creates a column called `id` with the data type `INT64`.
- `name STRING`: This part of the code creates a column called `name` with the data type `STRING`.
- `age INT64`: This part of the code creates a column called `age` with the data type `INT64`.

For more information on how to use BigQuery to define data types, please refer to the following links:
- [Defining Data Types in BigQuery](https://cloud.google.com/bigquery/docs/data-types)
- [Data Types in Standard SQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)

onelinerhub: [How do I use Google Big Query to define data types?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-to-define-data-types)