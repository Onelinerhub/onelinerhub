# How do I join two tables in Google BigQuery?
// plain

Joining two tables in Google BigQuery is done using the `JOIN` clause. An example of how to join two tables is shown below:

```
SELECT *
FROM table1 t1
JOIN table2 t2
ON t1.id = t2.id
```

This query will return all rows from both tables that have a matching `id` value in both tables.

The code above is composed of the following parts:

- `SELECT *` - This statement specifies which columns should be returned in the results. In this example, all columns will be returned.
- `FROM table1 t1` - This statement specifies which table should be used for the query. In this example, the `table1` table will be used and will be referred to as `t1` in the query.
- `JOIN table2 t2` - This statement specifies which table should be joined to the first table. In this example, the `table2` table will be joined to `table1` and will be referred to as `t2` in the query.
- `ON t1.id = t2.id` - This statement specifies the condition for the join. In this example, the join will be done on rows that have the same `id` value in both tables.

For more information, please see the [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/).

onelinerhub: [How do I join two tables in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-join-two-tables-in-google-bigquery)