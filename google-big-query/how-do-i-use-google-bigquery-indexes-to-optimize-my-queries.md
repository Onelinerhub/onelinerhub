# How do I use Google BigQuery indexes to optimize my queries?
// plain

Google BigQuery indexes are used to optimize queries by allowing the query engine to quickly identify and retrieve the data it needs. To create an index, you must first create a table, then specify which columns you want to index. For example, the following code creates a table called `mytable` and creates an index on the `column1` and `column2` columns:

```
CREATE TABLE mytable (
  column1 INT64,
  column2 INT64
)

CREATE INDEX mytable_index ON mytable (column1, column2)
```

Once the index is created, the query engine can use the index to quickly identify and retrieve the data it needs. This can significantly reduce query execution time and improve query performance.

## Code explanation


1. `CREATE TABLE mytable (column1 INT64, column2 INT64)`: This creates a table called `mytable` with two columns, `column1` and `column2`, both of which are of type INT64.

2. `CREATE INDEX mytable_index ON mytable (column1, column2)`: This creates an index called `mytable_index` on the `column1` and `column2` columns of the `mytable` table.

3. `SELECT * FROM mytable WHERE column1 = 1 AND column2 = 2`: This query uses the index to quickly identify and retrieve the data it needs.

## Helpful links

- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [Indexing in Google BigQuery](https://cloud.google.com/bigquery/docs/indexes)

onelinerhub: [How do I use Google BigQuery indexes to optimize my queries?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-indexes-to-optimize-my-queries)