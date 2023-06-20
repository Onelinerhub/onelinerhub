# How do I use Google Big Query SQL for software development?
// plain

Google BigQuery is a cloud-based data warehouse platform that allows developers to write SQL queries to interact with large datasets. To use BigQuery SQL for software development, developers need to create a dataset and upload data into it. Once the data is uploaded, developers can write SQL queries to retrieve, manipulate, and analyze the data.

For example, the following query can be used to select all records from a table called `users`:

```
SELECT * FROM users;
```

This query will return all records from the `users` table.

The following query can be used to filter the records in the `users` table by age:

```
SELECT * FROM users WHERE age > 18;
```

This query will return all records from the `users` table where the age of the user is greater than 18.

In addition to querying data, BigQuery SQL can also be used to create tables, insert data into tables, delete data from tables, and update existing data.

Here is an example of a query to create a new table:

```
CREATE TABLE orders (
  order_id INTEGER,
  customer_id INTEGER,
  order_date DATE
);
```

This query will create a new table called `orders` with three columns: `order_id`, `customer_id`, and `order_date`.

## Helpful links
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [BigQuery SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/)

onelinerhub: [How do I use Google Big Query SQL for software development?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-sql-for-software-development)