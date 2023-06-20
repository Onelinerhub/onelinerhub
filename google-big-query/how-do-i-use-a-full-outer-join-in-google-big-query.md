# How do I use a full outer join in Google Big Query?
// plain

A full outer join in Google Big Query combines the results of both left and right outer joins. It returns all rows from both tables, filling with null values where data is missing. The syntax is as follows:

```
SELECT *
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
```

The example above will return all rows from both tables, and null values where the join condition is not met.

## Code explanation


1. `SELECT *` - This is used to select all columns from the tables.
2. `FROM table1` - This specifies the first table to join.
3. `FULL OUTER JOIN table2` - This specifies the type of join (in this case, a full outer join) and the second table to join.
4. `ON table1.column_name = table2.column_name` - This specifies the join condition.

## Helpful links

- [Google BigQuery Documentation - Full Outer Join](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#full-outer-join)
- [Stackoverflow - Full Outer Join in Google BigQuery](https://stackoverflow.com/questions/46052964/full-outer-join-in-google-bigquery)

onelinerhub: [How do I use a full outer join in Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-use-a-full-outer-join-in-google-big-query)