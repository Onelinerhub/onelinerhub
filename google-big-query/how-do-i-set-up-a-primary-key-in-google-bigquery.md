# How do I set up a primary key in Google BigQuery?
// plain

Setting up a primary key in Google BigQuery is fairly simple. First, you must create a table in BigQuery. To do this, you can use the `CREATE TABLE` statement. For example:

```
CREATE TABLE my_table (
  id INT64,
  name STRING,
  age INT64
);
```

Once the table is created, you can set the primary key by using the `ALTER TABLE` statement. For example:

```
ALTER TABLE my_table ADD PRIMARY KEY (id);
```

The parts of the code are:

- `CREATE TABLE`: Used to create a new table.
- `ALTER TABLE`: Used to modify an existing table.
- `ADD PRIMARY KEY`: Used to set the primary key of the table.

## Helpful links

- [BigQuery Documentation: CREATE TABLE](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table)
- [BigQuery Documentation: ALTER TABLE](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#alter_table)

onelinerhub: [How do I set up a primary key in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-set-up-a-primary-key-in-google-bigquery)