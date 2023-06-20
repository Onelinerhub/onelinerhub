# How do I create a primary key in Google Big Query?
// plain

Creating a primary key in Google Big Query requires the use of the CREATE TABLE statement. The statement is used to define the columns of the table and the primary key. The primary key must be an existing column of the table and must be declared as such.

## Example

```
CREATE TABLE my_table (
  id INT64 NOT NULL,
  name STRING,
  PRIMARY KEY (id)
);
```

This statement will create a table called `my_table` with two columns, `id` and `name`. The `id` column will be the primary key and will be of type `INT64`, meaning it must be a 64-bit integer.

Parts of the code:

- `CREATE TABLE my_table`: This statement creates a table with the name `my_table`.
- `id INT64 NOT NULL`: This statement defines the `id` column as an `INT64` type and sets the `NOT NULL` constraint, meaning that its value must not be empty.
- `name STRING`: This statement defines the `name` column as a `STRING` type.
- `PRIMARY KEY (id)`: This statement declares the `id` column as the primary key for the table.

## Helpful links

- [CREATE TABLE statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#create_table)
- [Data types in BigQuery](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)

onelinerhub: [How do I create a primary key in Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-create-a-primary-key-in-google-big-query)