# How do I delete a Google Big Query table?
// plain

1. To delete a Google BigQuery table, you can use the `DELETE` statement.

2. For example, the following code block will delete the table `mydataset.mytable`:
```
DELETE FROM mydataset.mytable
```
3. If the table is successfully deleted, the output will be `Query OK, 0 rows affected (0.00 sec)`.

4. The `DELETE` statement can also be used with a `WHERE` clause to delete specific rows from a table.

5. For example, the following code block will delete all rows from `mydataset.mytable` that have a `value` greater than 10:
```
DELETE FROM mydataset.mytable WHERE value > 10
```
6. If the rows are successfully deleted, the output will be `Query OK, n rows affected (x.xx sec)`, where `n` is the number of rows deleted and `x.xx` is the execution time of the query.

7. For more information about deleting tables and rows in Google BigQuery, please refer to the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language).

onelinerhub: [How do I delete a Google Big Query table?](https://onelinerhub.com/google-big-query/how-do-i-delete-a-google-big-query-table)