# How do I use wildcards in Google BigQuery?
// plain

Wildcards are used in Google BigQuery to match patterns of strings in queries. Wildcards can be used in the SELECT, FROM, WHERE, and JOIN clauses of a query.

For example, the following query uses the `LIKE` operator with a wildcard to match a pattern of strings:

```
SELECT *
FROM table_name
WHERE column_name LIKE '%string%'
```

The `%` wildcard matches any string of any length (including an empty string). In the example above, the query will return all rows from the `table_name` table where the `column_name` contains the string `string`.

In addition to the `%` wildcard, BigQuery also supports the `_` wildcard, which matches any single character. For example:

```
SELECT *
FROM table_name
WHERE column_name LIKE 'str_ng'
```

The query above will return all rows from the `table_name` table where the `column_name` contains the string `str_ng`.

It is also possible to use multiple wildcards in a single query. For example:

```
SELECT *
FROM table_name
WHERE column_name LIKE '%str__ng%'
```

The query above will return all rows from the `table_name` table where the `column_name` contains the string `str__ng`, where `_` represents any single character.

For more information on using wildcards in BigQuery, please refer to the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical).

onelinerhub: [How do I use wildcards in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-use-wildcards-in-google-bigquery)