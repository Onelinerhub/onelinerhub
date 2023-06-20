# How do I use the UNION clause in Google BigQuery?
// plain

The UNION clause allows you to combine the results of two or more SELECT queries into a single result set. To use the UNION clause in Google BigQuery, you must specify the same number of columns in each SELECT query. The data type of the columns must also be the same.

For example, the following query combines the results of two SELECT queries:

```
SELECT name, age
FROM `dataset.table1`
UNION
SELECT name, age
FROM `dataset.table2`
```

The output of this query would be a single result set containing the combined results of both SELECT queries.

The parts of the example code are as follows:

1. `SELECT name, age` - This specifies the columns to be returned in the result set.
2. `FROM `dataset.table1`` - This specifies the source table for the first SELECT query.
3. `UNION` - This specifies that the results of the two SELECT queries should be combined.
4. `FROM `dataset.table2`` - This specifies the source table for the second SELECT query.

For more information on using the UNION clause in Google BigQuery, see the [official documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#union-clause).

onelinerhub: [How do I use the UNION clause in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-use-the-union-clause-in-google-bigquery)