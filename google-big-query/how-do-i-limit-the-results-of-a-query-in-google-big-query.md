# How do I limit the results of a query in Google Big Query?
// plain

To limit the results of a query in Google Big Query, you can use the `LIMIT` clause. This clause takes an integer as the argument, which is the maximum number of rows that will be returned by the query.

For example, the following query will return only the first 10 rows of the `bigquery-public-data.usa_names.usa_1910_2013` table:
```
SELECT *
FROM `bigquery-public-data.usa_names.usa_1910_2013`
LIMIT 10
```

The output of this query will be:
```
+--------+-------+------+-------+
|  name  | state | sex  | count |
+--------+-------+------+-------+
| Mary   | CA    | F    |   619 |
| Helen  | CA    | F    |   531 |
| Dorothy| CA    | F    |   476 |
| Margaret| CA   | F    |   467 |
| Ruth   | CA    | F    |   415 |
| Anna   | CA    | F    |   394 |
| Elizabeth| CA  | F    |   394 |
| Frances| CA    | F    |   340 |
| Marie  | CA    | F    |   327 |
| Mildred| CA    | F    |   305 |
+--------+-------+------+-------+
```

The `LIMIT` clause consists of the following parts:

- `LIMIT`: This is the keyword that tells BigQuery to limit the number of rows returned.
- `10`: This is the argument that tells BigQuery to return a maximum of 10 rows.

## Helpful links
- [BigQuery Documentation - LIMIT Clause](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#limit-clause)

onelinerhub: [How do I limit the results of a query in Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-limit-the-results-of-a-query-in-google-big-query)