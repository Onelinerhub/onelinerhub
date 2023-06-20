# How do I use Google BigQuery LIKE statements?
// plain

Google BigQuery provides the `LIKE` statement to allow users to filter query results based on a pattern. The pattern is specified using wildcard characters `_` and `%`. The `_` character matches any single character, while the `%` character matches any sequence of characters.

For example, the following query uses the `LIKE` statement to find all records with a name starting with `John`:

```sql
SELECT *
FROM `my_table`
WHERE name LIKE 'John%'
```

This query will return all records from the `my_table` table with a name that starts with `John`.

The following query uses the `LIKE` statement to find all records with a name ending with `Smith`:

```sql
SELECT *
FROM `my_table`
WHERE name LIKE '%Smith'
```

This query will return all records from the `my_table` table with a name that ends with `Smith`.

The following query uses the `LIKE` statement to find all records with a name containing `John`:

```sql
SELECT *
FROM `my_table`
WHERE name LIKE '%John%'
```

This query will return all records from the `my_table` table with a name that contains `John`.

## Helpful links

- [Google BigQuery Documentation - LIKE](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#like-operator)
- [Google BigQuery Documentation - Wildcard Characters](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#wildcard-characters)

onelinerhub: [How do I use Google BigQuery LIKE statements?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-like-statements)