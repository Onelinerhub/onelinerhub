# How do I query Google BigQuery using XML?
// plain

XML is not a supported query language for Google BigQuery. Instead, you should use the BigQuery Standard SQL syntax.

For example, the following query retrieves the total number of user sessions for each user:
```
SELECT user_id, COUNT(*) AS total_sessions
FROM `project.dataset.sessions_table`
GROUP BY user_id
```

The output of this query would be a table with two columns: `user_id` and `total_sessions`:
```
+---------+---------------+
| user_id | total_sessions|
+---------+---------------+
|    1234 |            10 |
|    5678 |            15 |
|    9012 |            20 |
+---------+---------------+
```

The query consists of three parts:

1. The `SELECT` clause which defines the columns to be returned in the results.
2. The `FROM` clause which defines the table from which the data should be retrieved.
3. The `GROUP BY` clause which defines the column by which the data should be grouped.

For more information, see the [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I query Google BigQuery using XML?](https://onelinerhub.com/google-big-query/how-do-i-query-google-bigquery-using-xml)