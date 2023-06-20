# How do I use Google Big Query to merge data?
// plain

Google BigQuery is a powerful tool for merging data from multiple sources. To use BigQuery to merge data, you will first need to create a table in BigQuery. The table should include the columns you want to merge, such as the names of the data sources, the columns you want to merge, and the type of data in each column.

Once the table is created, you can use the `MERGE` statement in BigQuery to combine the data from multiple sources.

The `MERGE` statement has the following syntax:

```
MERGE INTO <target_table> AS t
USING <source_table> AS s
ON <join_condition>
WHEN MATCHED THEN
  UPDATE SET t.<column_name> = s.<column_name>
WHEN NOT MATCHED THEN
  INSERT (<column_name>, ...) VALUES (s.<column_name>, ...)
```

The `MERGE` statement has the following parts:

* `target_table`: The table you want to merge the data into.
* `source_table`: The table you want to merge the data from.
* `join_condition`: The condition used to determine which rows to merge from the source table.
* `column_name`: The columns you want to merge.

For example, let's say you have two tables, `customers` and `orders`, and you want to merge the `customer_name` column from the `customers` table into the `orders` table. The `MERGE` statement would look like this:

```
MERGE INTO orders AS t
USING customers AS s
ON t.customer_id = s.customer_id
WHEN MATCHED THEN
  UPDATE SET t.customer_name = s.customer_name
```

This `MERGE` statement will take the `customer_name` column from the `customers` table and merge it into the `orders` table.

For more information on using BigQuery to merge data, see the [Google BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language).

onelinerhub: [How do I use Google Big Query to merge data?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-to-merge-data)