# How do I access the information_schema in Google BigQuery?
// plain

To access the information_schema in Google BigQuery, you can use the following query:

```sql
SELECT * FROM information_schema.tables
```

This query will return a list of all tables in the currently selected dataset.

The query consists of the following parts:

1. `SELECT *`: This is the clause that specifies the columns that should be returned in the result set. In this case, all columns are returned.

2. `FROM information_schema.tables`: This is the clause that specifies the table from which the data should be retrieved. In this case, the `information_schema.tables` table is used.

The output of the query will be a list of all tables in the currently selected dataset, with information about each table, such as its name, type, and creation date.

For more information about the information_schema in BigQuery, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/information-schema-intro).

onelinerhub: [How do I access the information_schema in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-access-the-information-schema-in-google-bigquery)